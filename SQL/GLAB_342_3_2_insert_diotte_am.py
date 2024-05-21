def calculate(nat_num):
    potential_factor = nat_num - 1
    factors = list()
    result = nat_num//potential_factor
    
    while result > 1 and potential_factor > 1:
        print(nat_num, potential_factor, result)
        if nat_num % potential_factor == 0:
            result = nat_num/potential_factor
            factors.append(result)
            nat_num = nat_num//result
            potential_factor = nat_num - 1
        else:        
            potential_factor -= 1
    if nat_num % potential_factor == 0:
            factors.append(nat_num)

    print(factors)

calculate(48)