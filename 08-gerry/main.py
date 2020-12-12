import random
import data


#Populate a 6x3 state with random 0's and 1's
#0's represent one type of voter (Dems)
#1's represent the other (Republican)
def makeState():
    row_num = int(6)
    col_num = int(3)
    return [[random.randint(0, 1) for col in range(col_num)]
            for row in range(row_num)]


#Prints the grid with 0's and 1's
def printState():
    for row in state:
        for item in row:
            print(str(item), end=" ")
        print()




# Create a dictionary for each district
def districts_by_row():
    #eacg row is a district
    districts = []
    for dist in range(1, 7):
        district = {}
        district['id'] = dist
        district['coordinates'] = [[dist - 1, 0], [dist - 1, 1], [dist - 1, 2]]
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
    for col in range(0, 3):
        for row in range(0, 3):
            coords.append([row, col])
        district['id'] = district_index
        district['coordinates'] = coords
        districts.append(district)
        coords = []
        district = {}
        district_index += 1
        for row in range(3, 6):
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
    district['coordinates'] = [[0, 0], [1, 0], [0, 1]]
    districts.append(district)
    district = {}
    district['id'] = 2
    district['coordinates'] = [[0, 2], [1, 1], [1, 2]]
    districts.append(district)
    district = {}
    district['id'] = 3
    district['coordinates'] = [[2, 0], [3, 0], [2, 1]]
    districts.append(district)
    district = {}
    district['id'] = 4
    district['coordinates'] = [[2, 2], [3, 1], [3, 2]]
    districts.append(district)
    district = {}
    district['id'] = 5
    district['coordinates'] = [[4, 0], [5, 0], [4, 1]]
    districts.append(district)
    district = {}
    district['id'] = 6
    district['coordinates'] = [[4, 2], [5, 1], [5, 2]]
    districts.append(district)
    return districts


# Determine the win based on the values of the cell
# and the coordinates contained in a district
# aaaaannndddd Add WIN to the dictionary
def determineWin(district):
    coords = district.get('coordinates')
    sum = 0
    for loc in coords:
        sum = sum + state[loc[0]][loc[1]]
    if sum < 2:
        district['winner'] = 0
    else:
        district['winner'] = 1


#Referencing the District Shapes kTs
# https://drive.google.com/file/d/1M5PW9EGIsXVpCzIaLWBx9BAxPBDbdQKL/view?usp=sharing
def A_District(row, col):
    return [[row, col], [row, col + 1], [row, col + 2]]

def A_available(row, col, map):
  #Map defaults to zero
  #If the sum is greater than zero then at least one space is taken
  if row < 6 and col + 2 < 3:
    return map[row][col] + map[row][col + 1]+map[row] [col + 2] == 0
  else:
    return False

def B_District(row, col):
    return [[row, col], [row, col + 1], [row + 1, col]]

def B_available(row, col, map):
  #Map defaults to zero
  #If the sum is greater than zero then at least one space is taken
  if row + 1 < 6 and col + 1 < 3:
    return map[row][col] + map[row][col + 1]+map[row + 1] [col] == 0
  else:
    return False;

def C_District(row, col):
    return [[row, col], [row, col + 1], [row + 1, col + 1]]

def C_available(row, col, map):
  #Map defaults to zero
  #If the sum is greater than zero then at least one space is taken
  if row + 1 < 6 and col + 1 < 3:
    return map[row][col] + map[row][col + 1]+map[row + 1] [col + 1] == 0
  else:
    return False


def D_District(row, col):
    return [[row, col], [row + 1, col], [row + 2, col]]

def D_available(row, col, map):
  #Map defaults to zero
  #If the sum is greater than zero then at least one space is taken
  if row + 2 < 6 and col < 3:
    return map[row][col] + map[row + 1][col]+map[row + 2] [col] == 0
  else:
    return False

def E_District(row, col):
    return [[row, col], [row + 1, col], [row + 1, col + 1]]

def E_available(row, col, map):
  #Map defaults to zero
  #If the sum is greater than zero then at least one space is taken
  if row + 1 < 6 and col + 1 < 3:
    return map[row][col] + map[row + 1][col]+map[row + 1] [col + 1] == 0
  else:
    return False

def L_District(row, col):
    return [[row, col], [row + 1, col], [row + 1, col - 1]]

def L_available(row, col, map):
  #Map defaults to zero
  #If the sum is greater than zero then at least one space is taken
  if row + 1 < 6 and col - 1 > -1:
    return map[row][col] + map[row + 1][col]+map[row + 1][col - 1] == 0
  else:
    return False



#Each Scheme has a grid of X's for taken coordinates, and blanks for available coordinates

#Creates the starter scheme
#Returns a scheme list with 2 items: a district map filled with zeros AND an empty list of districts
def starter_scheme():  
  scheme = []
  dist_map = [[0 for col in range(3)]for col in range(6)]
  districts = []
  scheme.append(dist_map)
  scheme.append(districts)
  return scheme
  
  
def printDistMap(map):
    for row in map:
        for item in row:
            print(str(item), end=" ")
        print()  
  


# Makes a COPY of the scheme so that the copy does NOT have pointers to the same exact data.
def copyScheme(scheme):
  dist_map = scheme[0]
  dist_list = scheme[1]
  
  noob = []

  noob_map = []
  for row in dist_map:
    noob_map.append(row.copy())
  
  noob_list = []
  for dist in dist_list:
    noob_list.append(dist.copy())
  
  noob.append(noob_map)
  noob.append(noob_list)

  return noob

  
# Prints the maps and districts for each Gerry Scheme
def print_Gerry_Schemes():
  for scheme in Gerry_Schemes:
    print("\nDistrict Map")
    #isolate the map and districts
    map = scheme[0]
    districts = scheme[1]
    #add wins
    for dist in districts:
      determineWin(dist)
    #print map
    for row in range(0,6):
      for col in range(0,3):
        print(map[row][col],end="")
      print("")
    #print districts
    for dist in districts:
      print(dist)
    #print winner
    print("winner: " + str(scheme_winner(districts)))
    


def remove_invalid_Gerry_Schemes():
  idx = 0
  while idx < len(Gerry_Schemes) and idx >-1:
    scheme = Gerry_Schemes[idx]
    districts = scheme[1]
    #if districts is smaller than 6, delete scheme
    if(len(districts)<6):
      Gerry_Schemes.remove(scheme)
      idx-=1
    idx+=1



def scheme_winner(districts):
  winner_sum = 0
  for dist in districts:
    winner_sum += dist['winner']
  if winner_sum < 3:
    data.num_zero_wins += 1
    return 0
  elif winner_sum >3:
    data.num_one_wins += 1
    return 1
  else:
    data.num_ties += 1
    return "tie"




#GENERATE START
state = makeState()
printState()
Gerry_Schemes  = []
Gerry_Schemes.append(starter_scheme())

#REDUNDANT!!! PASS FUNCTION AS ARGUMENT???
for row in range (0,6):
  for col in range(0,3):
    scheme_Idx = 0
    while scheme_Idx < len(Gerry_Schemes):
      # isolate the map and districts in the current scheme
      currScheme = Gerry_Schemes[scheme_Idx]
      dist_map = currScheme[0]
      districts = currScheme[1]
      # check map to see if you can make dist shape at given index
      if A_available(row, col, dist_map):
        #make a copy of the scheme and add district
        new_scheme = copyScheme(currScheme)
        new_map = new_scheme[0]
        new_districts = new_scheme[1]
        #create the district
        district = {}
        district['id'] = (len(districts) + 1)
        district['coordinates'] = A_District(row, col)
        #add the new district to the new scheme's list of districts 
        new_districts.append(district)
        #update the map 
        for coord in district['coordinates']:
           new_map[coord[0]][coord[1]] = district['id']
        #add the new scheme to the Gerry_Schemes list
        Gerry_Schemes.insert(scheme_Idx, new_scheme)
        #increase the index by one so the new scheme does not get read
        scheme_Idx += 1
      #end if A_available

      # check map to see if you can make dist shape at given index
      if B_available(row, col, dist_map):
        #make a copy of the scheme and add district
        new_scheme = copyScheme(currScheme)
        new_map = new_scheme[0]
        new_districts = new_scheme[1]
        #create the district
        district = {}
        district['id'] = (len(districts) + 1)
        district['coordinates'] = B_District(row, col)
        #add the new district to the new scheme's list of districts 
        new_districts.append(district)
        #update the map 
        for coord in district['coordinates']:
           new_map[coord[0]][coord[1]] = district['id']
        #add the new scheme to the Gerry_Schemes list
        Gerry_Schemes.insert(scheme_Idx, new_scheme)
        #increase the index by one so the new scheme does not get read
        scheme_Idx += 1
      #end if B_available
      
      # check map to see if you can make dist shape at given index
      if C_available(row, col, dist_map):
        #make a copy of the scheme and add district
        new_scheme = copyScheme(currScheme)
        new_map = new_scheme[0]
        new_districts = new_scheme[1]
        #create the district
        district = {}
        district['id'] = (len(districts) + 1)
        district['coordinates'] = C_District(row, col)
        #add the new district to the new scheme's list of districts 
        new_districts.append(district)
        #update the map 
        for coord in district['coordinates']:
           new_map[coord[0]][coord[1]] = district['id']
        #add the new scheme to the Gerry_Schemes list
        Gerry_Schemes.insert(scheme_Idx, new_scheme)
        #increase the index by one so the new scheme does not get read
        scheme_Idx += 1
      #end if C_available

      # check map to see if you can make dist shape at given index
      if D_available(row, col, dist_map):
        #make a copy of the scheme and add district
        new_scheme = copyScheme(currScheme)
        new_map = new_scheme[0]
        new_districts = new_scheme[1]
        #create the district
        district = {}
        district['id'] = (len(districts) + 1)
        district['coordinates'] = D_District(row, col)
        #add the new district to the new scheme's list of districts 
        new_districts.append(district)
        #update the map 
        for coord in district['coordinates']:
           new_map[coord[0]][coord[1]] = district['id']
        #add the new scheme to the Gerry_Schemes list
        Gerry_Schemes.insert(scheme_Idx, new_scheme)
        #increase the index by one so the new scheme does not get read
        scheme_Idx += 1
      #end if D_available

      # check map to see if you can make dist shape at given index
      if E_available(row, col, dist_map):
        #make a copy of the scheme and add district
        new_scheme = copyScheme(currScheme)
        new_map = new_scheme[0]
        new_districts = new_scheme[1]
        #create the district
        district = {}
        district['id'] = (len(districts) + 1)
        district['coordinates'] = E_District(row, col)
        #add the new district to the new scheme's list of districts 
        new_districts.append(district)
        #update the map 
        for coord in district['coordinates']:
           new_map[coord[0]][coord[1]] = district['id']
        #add the new scheme to the Gerry_Schemes list
        Gerry_Schemes.insert(scheme_Idx, new_scheme)
        #increase the index by one so the new scheme does not get read
        scheme_Idx += 1
      #end if E_available

      # check map to see if you can make dist shape at given index
      if L_available(row, col, dist_map):
        #make a copy of the scheme and add district
        new_scheme = copyScheme(currScheme)
        new_map = new_scheme[0]
        new_districts = new_scheme[1]
        #create the district
        district = {}
        district['id'] = (len(districts) + 1)
        district['coordinates'] = L_District(row, col)
        #add the new district to the new scheme's list of districts 
        new_districts.append(district)
        #update the map 
        for coord in district['coordinates']:
           new_map[coord[0]][coord[1]] = district['id']
        #add the new scheme to the Gerry_Schemes list
        Gerry_Schemes.insert(scheme_Idx, new_scheme)
        #increase the index by one so the new scheme does not get read
        scheme_Idx += 1
      #end if L_available

      scheme_Idx += 1

      # Gerry_Schemes.remove(currScheme)
    # end while scheme_Idx < len(Gerry_Schemes)



remove_invalid_Gerry_Schemes()
print("Gerry Schemes")     
print_Gerry_Schemes()
print("\nNumber of schemes: " + str(len(Gerry_Schemes)))
print("Number 0 wins: " + str(data.num_zero_wins))
print("Number 1 wins: " + str(data.num_one_wins))
print("Number Ties: " + str(data.num_ties))
if data.num_zero_wins > data.num_one_wins:
  print("Party Zero Wins")
elif data.num_one_wins > data.num_zero_wins:
  print("Party One Wins")
else:
  print("Parties Zero and One are tied")



