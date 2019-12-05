wires = open("input.txt").readlines()

def parse(wire_as_string) -> list:
    return [(instruction[0],int(instruction[1:])) for instruction in wire_as_string.split(",")]

def calculate_all_positions(wire_instructions) -> list:
    all_positions = []
    position = [0,0]
    for instruction in wire_instructions:
        direction, amount = instruction
        for i in range(amount):
            if direction == "L":
                position[0] -= 1
            if direction == "R":
                position[0] += 1
            if direction == "U":
                position[1] += 1
            if direction == "D":
                position[1] -= 1
            all_positions.append(position.copy())
    return all_positions

positions = calculate_all_positions(parse(wires[0]))
positions2 = calculate_all_positions(parse(wires[1]))

for pos in positions:
    if pos in positions2:
        print(pos)
