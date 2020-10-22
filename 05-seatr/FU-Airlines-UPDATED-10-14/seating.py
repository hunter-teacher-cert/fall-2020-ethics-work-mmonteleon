import data
import graphics

def seat_cheapos():
  for party in data.unseated_parties_indices:
    for passenger in data.parties[party]:
      row, col = data.next_available_seat()
      data.seating_chart[row][col] = passenger
      data.passengers[passenger]['seat'] = str(row+1)+graphics.col_to_letter(col)
      data.seating_chart_by_party[row][col] = party