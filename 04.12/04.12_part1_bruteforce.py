total = 0
for i in range(272091,815433): #Outer bound is exclusive
    digits = [int(x) for x in list(str(i))]
    previous, has_double = -1, False
    for digit in digits:
        if digit < previous:
            break #Continue with outer for loop, do not execute else
        if digit == previous:
            has_double = True
        previous = digit
    else: #If this is reached, the number is non-decreasing
        total += has_double #only increments it if there was a double
    
