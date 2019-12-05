total = 0
for i in range(272091,815433): #Outer bound is exclusive
    digits = [int(x) for x in list(str(i))]
    previous = -1
    duplicates = []
    current_duplicate_amt = 0
    for digit in digits:
        if digit < previous:
            break #Continue with outer for loop, do not execute else
        if digit == previous:
            if current_duplicate_amt==0:
                duplicates.append(digit)
            elif current_duplicate_amt==1: #Remove last duplicate only in this case, as this is the step that invalidates it
                duplicates.pop()
            current_duplicate_amt += 1
        else:
            current_duplicate_amt = 0
        previous = digit
    else: #If this is reached, the number is non-decreasing
        total += bool(duplicates)
    
