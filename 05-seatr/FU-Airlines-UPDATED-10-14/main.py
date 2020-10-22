import data
import graphics
import buy_tickets
import seating

graphics.print_title()
graphics.print_finger()



# Part I: Purchasing tickets
  #  Buy ticket(s)
  #  Choose: Pay to pick seat or nah...
  #  if pay for seat, show chart, user picks seats. 
  #  else put in a list ()
suckers_available = input("Do you want to purchase tickets for FU Airlines?\n")
while(not (suckers_available == 'n'or suckers_available == 'N' or suckers_available == 'no' or suckers_available == 'No')):
  buy_tickets.buy_ticket()
  suckers_available = input("Are there any more suckers available to purchase tickets for FU Airlines?\n")
print("FU and Have a nice day!")


#   Part II: Sales done.  Seating algo time.
  # cheapos get seated zig-zag style in empty seats from front to back
seating.seat_cheapos()
#Visual of the parties:  The plane seats are labeled with party ID to make it easier to identify which parties are seated together
graphics.print_seating_chart_by_party()

# I think we should create a database of to fill 3/4 of the plane so we can really see the algorithm.




