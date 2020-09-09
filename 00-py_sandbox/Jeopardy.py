import requests
import similar_text
from similar_text import similar_text

questions =[
  requests.get('http://jservice.io/api/clues?category=4469').json(),
  requests.get('http://jservice.io/api/clues?category=8031').json(),
  requests.get('http://jservice.io/api/clues?category=4778').json(),
  requests.get('http://jservice.io/api/clues?category=10927').json(),
  requests.get('http://jservice.io/api/clues?category=18399').json(),
  requests.get('http://jservice.io/api/clues?category=4888').json()
]

# Column is Category, Row is value
gameboard = [
  ["$100", "$100", "$100", "$100", "$100", "$100"],
  ["$200", "$200", "$200", "$200", "$200", "$200"],
  ["$300", "$300", "$300", "$300", "$300", "$300"],
  ["$400", "$400", "$400", "$400", "$400", "$400"],
  ["$500", "$500", "$500", "$500", "$500", "$500"]
  ]

categories = ["disney dogs", "disney song lyrics", "disney villians", "disney movie taglines", "disney 7 dwarfs", "disney anagrammed characters"]

money = 0

# Get category number (the column  index to be used in gameboard)
def get_category_number(category):
  for i in range(0,len(categories)):
    if categories[i].lower()==category.lower():
      return i
    elif similar_text(categories[i].lower(), category.lower()) > 85:
      return i
  return -1

# Get the row index in the gameboard for a given bet
def get_row_from_value(value):
  return int(value/100-1)


# Retrieves question given the category and question number
# parameters: category, question number
def getQuestion(category_num, question_num):
    return questions[category_num][question_num]["question"]

# Retrieves Answer given category and question number
def getAnswer(cat_num,question_num):
    ans = questions[cat_num][question_num]["answer"]
    ans = ans.replace("<i>", "")
    ans = ans.replace("</i>", "")
    return ans

# Checks answer, updates score and prints an appropriate respons
def checkAnswer(cat_num, question_num, user_response):
  no_the = getAnswer(cat_num, question_num).replace("The ","")
  if user_response.lower() == getAnswer(cat_num, question_num).lower():
    print("\nCorrect!")
    change_money(100*question_num + 100)
  #works even if the user skips "the"
  elif user_response.lower() == no_the.lower():
    print("\nCorrect!")
    change_money(100*question_num + 100)
  elif similar_text(user_response.lower(),getAnswer(cat_num, question_num).lower())>85:
    print("\nCorrect!")
    change_money(100*question_num + 100)
  else:
    print("Sorry that is not correct.")
    print("The correct answer is: " + getAnswer(cat_num, question_num))
    change_money(-100*question_num - 100)

# Prints jeopardy ascii art
def print_jeopardy_title():
    print("""
                                                                        __
                                                                        /  |
            __   ______    ______    ______    ______    ______    ____$$ | __    __
            /  | /      \  /      \  /      \  /      \  /      \  /    $$ |/  |  /  |
            $$/ /$$$$$$  |/$$$$$$  |/$$$$$$  | $$$$$$  |/$$$$$$  |/$$$$$$$ |$$ |  $$ |
            /  |$$    $$ |$$ |  $$ |$$ |  $$ | /    $$ |$$ |  $$/ $$ |  $$ |$$ |  $$ |
            $$ |$$$$$$$$/ $$ \__$$ |$$ |__$$ |/$$$$$$$ |$$ |      $$ \__$$ |$$ \__$$ |
            $$ |$$       |$$    $$/ $$    $$/ $$    $$ |$$ |      $$    $$ |$$    $$ |
      __   $$ | $$$$$$$/  $$$$$$/  $$$$$$$/   $$$$$$$/ $$/        $$$$$$$/  $$$$$$$ |
      /  \__$$ |                    $$ |                                    /  \__$$ |
      $$    $$/                     $$ |                                    $$    $$/
      $$$$$$/                      $$/                                      $$$$$$/
 """)



# Print Block
#  14 characters
def print_categories():
    print("---------------- ---------------- ---------------- ---------------- ---------------- ----------------")
    print("|    Disney    | |   Disney     | |    Disney    | |   Disney     | |     Disney   | |   Disney     |")
    print("|     Dogs     | | Song Lyrics  | |   Villians   | |   Movie      | |   7 Dwarfs   | |  Anagrammed  |")
    print("|              | |              | |              | |  Taglines    | |              | |  Characters  |")
    print("---------------- ---------------- ---------------- ---------------- ---------------- ----------------")

def print_gameboard():
  global gameboard
  for row in gameboard:
    for col in row:
      print("|     "+ col +"     |", end=" ")
    print("\n---------------- ---------------- ---------------- ---------------- ---------------- ----------------")

def get_category():
  category=""
  while(True):
    print("\nPlease pick a category OR type Q to quit: ")
    category=input()
    if category.lower() == "q":
      print("Laters!")
      return -1
    elif category.lower() in categories:
      break
    else:
      print("invalid entry")
  return(category, get_category_number(category))

def get_category_v2():
  category=""
  while(True):
    print("\nPlease pick a category OR type Q to quit: ")
    category=input()
    if category.lower() == "q":
      print("Laters!")
      return -1
    else:
      cat_num = get_category_number(category)
      if cat_num != -1:
        return(cat_num)
        break
      else:
        print("invalid entry")
  return(get_category_number(category))

def get_value(category_num):
  #Get user input
  while(True):
    print("\nPlease pick a value: $", end=" ")
    value = int(input())
    if value%100 == 0 and get_row_from_value(value) >= 0 and get_row_from_value(value) <= 5:
      # Check to make sure that that category is available
      row = get_row_from_value(value)
      if gameboard[row][category_num] != "xxxx":
        gameboard[row][category_num] = "xxxx"
        return row
        break
    else:
      print("invalid entry")

def get_money():
  global money
  print("\nYou have $"+ str(money))

def change_money(change):
  global money
  money = money + change


#GAME
count = 0
while(True):
  print_jeopardy_title()
  print_categories()
  print_gameboard()

  get_money()
  cat_num = get_category_v2()
  # If the cat_num is -1, that means the player chose to quit
  if(cat_num != -1):
    ques_num = get_value(cat_num)
    print("\nClue:")
    print(getQuestion(cat_num,ques_num))
    print("\nWhat is / Who are etc...? ", end ="")
    player_answer = input()
    checkAnswer(cat_num, ques_num, player_answer)
  else:
    break
  # When all questions have been exhasted, end game
  if count==30:
    print("That's all I've got.  Good Game")
    get_money()
    break

  print("\nPress any key to continue.")
  key_press=input()
