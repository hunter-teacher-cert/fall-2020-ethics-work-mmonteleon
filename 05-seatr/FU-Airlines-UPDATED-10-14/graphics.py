from data import seating_chart
from data import seating_chart_by_party



def print_title():
    print("""
 /$$$$$$$$ /$$   /$$        /$$$$$$  /$$           /$$ /$$                              
| $$_____/| $$  | $$       /$$__  $$|__/          | $$|__/                              
| $$      | $$  | $$      | $$  \ $$ /$$  /$$$$$$ | $$ /$$ /$$$$$$$   /$$$$$$   /$$$$$$$
| $$$$$   | $$  | $$      | $$$$$$$$| $$ /$$__  $$| $$| $$| $$__  $$ /$$__  $$ /$$_____/
| $$__/   | $$  | $$      | $$__  $$| $$| $$  \__/| $$| $$| $$  \ $$| $$$$$$$$|  $$$$$$ 
| $$      | $$  | $$      | $$  | $$| $$| $$      | $$| $$| $$  | $$| $$_____/ \____  $$
| $$      |  $$$$$$/      | $$  | $$| $$| $$      | $$| $$| $$  | $$|  $$$$$$$ /$$$$$$$/
|__/       \______/       |__/  |__/|__/|__/      |__/|__/|__/  |__/ \_______/|_______/ 
    """)

def print_finger():
  print("""             
                        _                         _
                       |_|                       |_|
                       | |         /^^^\         | |
                      _| |_      (| "o" |)      _| |_
                    _| | | | _    (_---_)    _ | | | |_
                   | | | | |' |    _| |_    | `| | | | |
                   |          |   /     \   |          |
                    \        /  / /(. .)\ \  \        /
                      \    /  / /  | . |  \ \  \    /
                        \  \/ /    ||Y||    \ \/  /
                         \__/      || ||      \__/
                                   () ()
                                   || ||
                                  ooO Ooo  
  """)

# This function conversts columns to letters
# Input: column number in plane
# Output: Seat Letter
def col_to_letter(col):
  if col == 0:
    return "A"
  elif col == 1:
    return "B"
  elif col == 2:
    return "C"
  elif col == 3:
    return "D"
  elif col == 4:
    return "E"
  else:
    return "F"

# This function conversts letters to column numbers
# Input: Seat Letter
# Output: Column Number
def letter_to_col(letter):
  if letter.upper() == "A":
    return 0
  elif letter.upper() == "B":
    return 1
  elif letter.upper() == "C":
    return 2
  elif letter.upper() == "D":
    return 3
  elif letter.upper() == "E":
    return 4
  else:
    return 5


def print_available_seats_chart():
  print("\n -----------   -----------   -----------                  -----------   -----------   -----------")
  for row in range(0,30):
    # Seat number alignment.  Add an extra single space to single digit rows.  To make the chart look pretty.
    if row < 9:
      extra_ch_space = " "
    else:
      extra_ch_space = ""
    for col in range(0,6):
      # Checks to see if an aise follows the seat.  Adds space to printout if necessary.
      if col == 2:
        aisle_space = "               "
      else:
        aisle_space = ""
      # Print Available seat numbers.  Taken seats are coded "XXX"
      if seating_chart[row][col] == -1:
        print("|    "+ str(row+1) + str(col_to_letter(col))+extra_ch_space+"    |" + aisle_space, end=" ")
      else:
        print("|    "+ "XXX" +"    |" + aisle_space, end=" ")
    print("\n -----------   -----------   -----------                  -----------   -----------   -----------")

def print_seating_chart_by_party():
  print("SEATING CHART BY PARTY")
  print("\n -----------   -----------   -----------                  -----------   -----------   -----------")
  for row in range(0,30):
    # Seat number alignment.  Add an extra single space to single digit rows.  To make the chart look pretty.
    for col in range(0,6):
      if type(seating_chart_by_party[row][col]) == int and seating_chart_by_party[row][col] < 10:
        extra_ch_space = "  "
      elif type(seating_chart_by_party[row][col]) == int and seating_chart_by_party[row][col] < 100:
        extra_ch_space = " "
      else:
        extra_ch_space = ""
      # Checks to see if an aise follows the seat.  Adds space to printout if necessary.
      if col == 2:
        aisle_space = "               "
      else:
        aisle_space = ""
      # Print Parties in Seats
      if seating_chart_by_party[row][col] != 'NA':
        print("|    "+ str(seating_chart_by_party[row][col])+extra_ch_space+"    |" + aisle_space, end=" ")
      else:
        print("|    "+ "NA " +"    |" + aisle_space, end=" ")
    print("\n -----------   -----------   -----------                  -----------   -----------   -----------") 