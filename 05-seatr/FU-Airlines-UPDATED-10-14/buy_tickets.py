import graphics
import data

def buy_ticket():
  party = []
  print("Welcome to FU Airlines!")
  nbrseat = input("How many tickets would you like?\n")
  x = input("Would you be purchasing a seat today?\n")
  i = 1
  
  #purchasing seat
  if x == "Y" or x == "y" or x == "yes" or x == "Yes":
    while i <= int(nbrseat):
      party.append(data.passenger_id)
      name = input("Enter passenger #{num}'s name: ".format(num = i))
      
      graphics.print_available_seats_chart()
      seat = input("Pick a seat number: ") # add availability check if seat picked is available
      
      #Create a dictionary object for the new passenger
      pass_dict = {}
      pass_dict['id'] = data.passenger_id
      pass_dict['name'] = name
      pass_dict['party'] = data.party_id
      pass_dict['seat'] = seat
      data.passengers.append(pass_dict)
      
      #update the plane's seating chart
      if len(seat) == 3:
        row = int(seat[0:2])
        col = graphics.letter_to_col(seat[2])
      else:
        row = int(seat[0:1])
        col = graphics.letter_to_col(seat[1])
      
      data.seating_chart[row-1][col] = data.passenger_id
      data.seating_chart_by_party[row-1][col] = data.party_id
      
      #increment the passenger_id AND loop index
      data.passenger_id += 1
      i += 1
  
  # NOT purchasing seat
  else:
    print("Since you didn't pay for your seat, you will get what you get, so don't get upset.")
    data.unseated_parties_indices.append(data.party_id)
    
    while i <= int(nbrseat):
      party.append(data.passenger_id)
      name = input("Enter passenger #{num}'s name: ".format(num = i))
      
      #Create a dictionary object for the new passenger
      pass_dict = {}
      pass_dict['id'] = data.passenger_id
      pass_dict['name'] = name
      pass_dict['party'] = data.party_id
      pass_dict['seat'] = "NA"
      data.passengers.append(pass_dict)
      
      #increment the passenger_id AND loop index
      data.passenger_id += 1
      i += 1
  
  #add the party to the parties list.
  data.parties.append(party)
  
  #increment the party_id
  data.party_id += 1
  print("Thank you for flying FU")





