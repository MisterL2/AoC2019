class Vector:
    def __init__(self,steps,x,y,endx,endy):
        self.x, self.y, self.steps, self.endx, self.endy = x, y, steps, endx, endy

    def overlapsAt(self,other): #Returns the overlap coords or none
        if (self.x < other.x) == (self.endx > other.endx) and (self.y < other.y) == (self.endy > other.endy): #overlaps
            return (self.x if self.x == self.endx else other.x, self.y if self.y == self.endy else other.y)

    def stepsTo(self,position: tuple):
        distance = (self.x-position[0] + self.y-position[1])
        return distance if distance>0 else -distance

            
wires = open("input.txt").readlines()

def parse(wire_as_string) -> list:
    return [(instruction[0],int(instruction[1:])) for instruction in wire_as_string.split(",")]

def calculate_all_vectors(wire_instructions) -> list:
    all_vectors = []
    steps = 0
    position = [0,0]
    for instruction in wire_instructions:
        direction, amount = instruction
        old_x, old_y = position[0], position[1]
        
        if direction == "L":
            position[0] -= amount
        if direction == "R":
            position[0] += amount
        if direction == "U":
            position[1] += amount
        if direction == "D":
            position[1] -= amount
            
        all_vectors.append(Vector(steps, old_x, old_y, position[0], position[1]))
        steps += amount #Must be at the end
    return all_vectors

vectors = calculate_all_vectors(parse(wires[0]))
vectors2 = calculate_all_vectors(parse(wires[1]))

for vector in vectors:
    for other_vector in vectors2:
        overlap = vector.overlapsAt(other_vector)
        if overlap:
            overlap_position = vector.overlapsAt(other_vector)
            steps = vector.steps + vector.stepsTo(overlap_position)
            otherSteps = other_vector.steps + other_vector.stepsTo(overlap_position)
            print(f"{overlap_position} : {steps + otherSteps}")
            
