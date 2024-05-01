f = open("currupt_file.txt")

try:
    # open file save to variable
    f = open('../../Users/amarediotte/DataEngineeringRepos/2024-RT-107_diotte-am/341_Advanced_Python/Exceptions/test_file.txt')
    
    # if f.name == 'cdurrupt_file.txt':
        # raise Exception
except FileNotFoundError as e:
    print("sorry, this file does not exist")
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')


print(f)
