import random

#Populate a 6x3 state with random 0's and 1's
#0's represent one type of voter (Dems)
#1's represent the other (Republican)
def makeState():
  row_num = int(6)
  col_num = int(3)
  return [[random.randint(0,1) for col in range(col_num)] for row in range(row_num)]

#Prints the grid with 0's and 1's
def printState():
  for row in state:
    for item in row:
      print(str(item),end=" ")
    print()

state = makeState()
printState()

# Create a dictionary for each district
def districts_by_row():
  #eacg row is a district
  districts = []
  for dist in range(1,7):
    district = {}
    district['id'] = dist
    district['coordinates'] = [[dist-1, 0], [dist-1, 1], [dist-1, 2]]
    districts.append(district)
  return districts

def districts_by_col():
  #each column has 2 districts
  #list of dictionaries
  districts = [] 
  #dictionary holds an 'id', and 'coordinates'
  district = {}  
  district_index = 1
  coords = []
  for col in range(0,3):
    for row in range(0,3):
      coords.append([row, col])
    district['id'] = district_index
    district['coordinates'] = coords
    districts.append(district)
    coords = []
    district = {}
    district_index += 1
    for row in range(3,6):
      coords.append([row, col])
    district['id'] = district_index
    district['coordinates'] = coords
    districts.append(district)
    coords = []
    district = {}
    district_index += 1 
  return districts

# Generates districts in L shapes
def districts_by_L():
  # starts with corner, and the adjacent down and left/right
   #list of dictionaries
  districts = [] 
  #dictionary holds an 'id', and 'coordinates'
  district = {}  
  district['id'] = 1
  district['coordinates'] = [[0,0],[1,0],[0,1]]
  districts.append(district)
  district = {}  
  district['id'] = 2
  district['coordinates'] = [[0,2],[1,1],[1,2]]
  districts.append(district)
  district = {}  
  district['id'] = 3
  district['coordinates'] = [[2,0],[3,0],[2,1]]
  districts.append(district)
  district = {}  
  district['id'] = 4
  district['coordinates'] = [[2,2],[3,1],[3,2]]
  districts.append(district)
  district = {}  
  district['id'] = 5
  district['coordinates'] = [[4,0],[5,0],[4,1]]
  districts.append(district)
  district = {}  
  district['id'] = 6
  district['coordinates'] = [[4,2],[5,1],[5,2]]
  districts.append(district)
  return districts

print()
print("By ROW")
districts_v1 = districts_by_row()
for dist in districts_v1:
  print(dist)

print("By COL")
districts_v2 = districts_by_col()
for dist in districts_v2:
  print(dist)

print("By L")
districts_v3 = districts_by_L()
for dist in districts_v3:
  print(dist)

