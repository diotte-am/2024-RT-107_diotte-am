import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {', '.join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}')
            line_count += 1
    print(f'Processed {line_count} lines.')


with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    month_log = [0,0,0,0,0,0,0,0,0,0,0,0]
    for row in csv_reader:
        month = row[2]
        match month:
            case 'January':
                month_log[0] += 1
            case "February":
                month_log[1] += 1
            case "March":
                month_log[2] += 1
            case "April":
                month_log[3] += 1
            case "May":
                month_log[4] += 1
            case "June":
                month_log[5] += 1
            case "July":
                month_log[6] += 1
            case "August":
                month_log[7] += 1
            case "September":
                month_log[8] += 1
            case "October":
                month_log[9] += 1
            case "November":
                month_log[10] += 1
            case "December":
                month_log[11] += 1
    print(month_log)

# Questions:
# 1) what percentage of employees are born in each month?
# 2) Which month has the highest percentage of employees?
# 3) Which department has the highest number of June birthdays?