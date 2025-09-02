for i in range(1, 101): #Loop through numbers from 1 to 100 (inclusive of 1, exclusive of 101)
    if i % 3 == 0 and i % 5 == 0: #Check if number is divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0: #check if number is divisible by 3
        print("Fizz")
    elif i % 5 == 0: #check if number is divisible by 5
        print("Buzz")
    else: #If not divisible by either 3 or 5
        print(i)
