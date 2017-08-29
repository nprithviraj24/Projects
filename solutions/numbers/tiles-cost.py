
length = input("Enter the length: ")
width = input("Enter the width: ")


print("\n Assuming the tile is rectangle")
l2 = input("Enter the length of the tile: ")
w2 = input("Enter the width of the tile: ")

cost = input("Enter the cost of tile: ")
area= float(length * width) 
a2=float( l2 * w2) 

print("\n\tArea of your room: "),
print(area)

TotalCost=float( area*cost/a2)  
print("\n\t Total cost: "),
print(TotalCost)
