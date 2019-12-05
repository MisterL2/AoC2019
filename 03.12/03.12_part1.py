class Vector:
    def __init__(self,x,y,endx,endy):
        self.x, self.y, self.endx, self.endy = x,y,endx,endy

    def overlapsAt(self,other): #Returns the overlap coords or none
        if (self.x < other.x) == (self.endx > other.endx) and (self.y < other.y) == (self.endy > other.endy): #overlaps
            return (self.x if self.x == self.endx else other.x, self.y if self.y == self.endy else other.y)

            
wires = open("input.txt").readlines()

def parse(wire_as_string) -> list:
    return [(instruction[0],int(instruction[1:])) for instruction in wire_as_string.split(",")]

def calculate_all_vectors(wire_instructions) -> list:
    all_vectors = []
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
            
        all_vectors.append(Vector(old_x, old_y, position[0], position[1]))
    return all_vectors

vectors = calculate_all_vectors(parse(wires[0]))
vectors2 = calculate_all_vectors(parse(wires[1]))

for vector in vectors:
    for other_vector in vectors2:
        overlap = vector.overlapsAt(other_vector)
        if overlap:
            print(vector.overlapsAt(other_vector))
