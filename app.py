def number_squared(num):
    return num ** 2

print(number_squared(5))

def largest_number(num_one, num_two, num_three):
    try:
        if(num_one >= num_two and num_one >= num_three):
            return num_one
        elif(num_two >= num_one and num_two >= num_three):
            return num_two
        else:
            return num_three
    except TypeError:
        print("Please enter 3 valid numbers")
    except:
        print("Something went wrong")
    

print(largest_number(1, 56, 0))