#!/usr/bin/env python
# coding: utf-8

"""
Amare Diotte
SBA 343 & 344 - Data Analysis and visualization with Python
Part 2 - Create Visualizations using Matplotlib, Seaborn & Folium

"""

import dash
import more_itertools
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# SETUP---------------------------------------------------------------------------------
# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)


# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics Report', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

# Complete list of years 
year_list = [i for i in range(1980, 2024, 1)]


# LAYOUT---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    # Dashboard title
    html.H1("Automobile Sales Statistics Dashboard", 
        style={'textAlign': 'center', 'color': "#503D36", 'font-size': 24}),
    # Dropdown menu
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            # menu contents
            options=[
                           {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                           {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                           ],
            value='Select Statistics',
            # default text
            placeholder='Select a report type'
        )
    ]),
    # iterates thru years list and populates dropdown
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value='Select Year'
        )),
    # container that will hold the graphs
    html.Div([
    html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),])
])

# CALLBACKS---------------------------------------------------------------------------------------

# This callback determines whether yearly or recession statistics will be shown (1st dropdown)
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics',component_property='value'))

def update_input_container(selected_statistics):
    if selected_statistics =='Yearly Statistics': 
        return False
    else: 
        return True

#Callback for plotting
# This callback returns a container with the chosen plots
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='select-year', component_property='value'), 
    Input(component_id='dropdown-statistics', component_property='value')])


def update_output_container(input_year, selected_statistics):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
# PLOTS---------------------------------------------------------------------------------------
    # Recession Data---------------------------------------------------------------------------------------
#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # find average number of sales by year
        yearly_rec=recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec, 
                x='Year',
                y='Automobile_Sales',
                title="Average Automobile Sales fluctuation over Recession Period"))

#Plot 2 Calculate the average number of vehicles sold by vehicle type       
        # find average number of old vehicles, group by vehicle type
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()                           
        R_chart2  = dcc.Graph(
            figure=px.line(average_sales, 
            x='Vehicle_Type', 
            y='Automobile_Sales',
            title="Average Auto Sales by Vehicle Type during Recession"))
        
# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # group by vehicle type and find the some of ad expenditure
        exp_rec= recession_data.groupby("Vehicle_Type")["Advertising_Expenditure"].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
            names='Vehicle_Type',
            values="Advertising_Expenditure",
            title="Total Expenditures by Vehicle Type During Recession",
            )
        )

# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        # group by unemployment and vehicle, take average of sales+
        unemp_rate = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemp_rate,
                x='unemployment_rate',
                y='Automobile_Sales',
                color="Vehicle_Type",
                title="Effects of Unemployment Rate on Automobile Sales by Vehicle Type during Recession Period"))

        # return html for container if recession
        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1),html.Div(children=R_chart2)]),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3),html.Div(children=R_chart4)])
            ]


    # Yearly Data---------------------------------------------------------------------------------------                          
    elif (input_year and selected_statistics=='Yearly Statistics') :
        yearly_data = data[data['Year'] == input_year]
                              

                              
        #plot 1 Yearly Automobile sales using line chart for the whole period.
        # get total sales, group by year
        yas= data.groupby('Year')['Automobile_Sales'].sum().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas,
            x='Year', y="Automobile_Sales",
            title="Automobile Sales for the Year"))
            
        # Plot 2 Total Monthly Automobile sales using line chart.
        # group year df by month, and get sum of auto sales
        tms = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(tms,
            x="Month",
            y="Automobile_Sales",
            title="Total Auto Sales by Month"
            )
        )

        # Plot bar chart for average number of vehicles sold during the given year
        # year df, group by vehicle type, get average of sales
        avr_vdata=yearly_data.groupby("Vehicle_Type")["Automobile_Sales"].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata, 
            x='Vehicle_Type',
            y='Automobile_Sales',
            title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

        # Total Advertisement Expenditure for each vehicle using pie chart
        # year df, group by vehicle, get sum of ad expenses
        exp_data=yearly_data.groupby('Vehicle_Type')["Advertising_Expenditure"].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data,
            values = "Advertising_Expenditure",
            names = "Vehicle_Type",
            title="Total Ad Expenditure by Vehicle Type")
        )

        # return container if graphs are yearly
        return [
                html.Div(className='chart-item', children=[html.Div(children=Y_chart1),html.Div(children=Y_chart2)]),
                html.Div(className='chart-item', children=[html.Div(children=Y_chart3),html.Div(children=Y_chart4)])
                ]
    # return nothing if no selection is made
    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)

