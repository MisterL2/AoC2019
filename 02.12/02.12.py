values = open("input.txt").read()

def parse(program_as_string) -> list:
    return [int(value) for value in program_as_string.split(",")]

def process(numberslist):
    i = 0
    while i+3 < len(numberslist):
        if operation(numberslist, i):
            break
        i+=4
    return numberslist

def operation(program, location):
    opcode = program[location]
    first = program[location+1]
    second = program[location+2]
    result_location = program[location+3]
    
    if opcode == 1:
        calculation_result = program[first] + program[second]
    elif opcode == 2:
        calculation_result = program[first] * program[second]
    elif opcode == 99:
        return True
    else:
        print("beep boop not good " + str(opcode))

    program[result_location] = calculation_result


#First puzzle

#print(process(parse(values)))


#Second puzzle, literal bruteforce

def get_values(noun, verb):
    numlist = parse(values)
    numlist[1], numlist[2] = noun, verb
    return numlist

for i in range(100):
    for j in range(100):
        if process(get_values(i,j))[0] == 19690720:
            print(i)
            print(j)
            break
