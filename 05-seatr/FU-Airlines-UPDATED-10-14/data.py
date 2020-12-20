row_num = int(30)
col_num = int(6)
seating_chart = [[-1 for col in range(col_num)] for row in range(row_num)]
seating_chart_by_party = [['NA' for col in range(col_num)] for row in range(row_num)]


fields = ['id', 'name', 'party','seat']
passengers = []
parties = []
unseated_parties_indices = []
party_id = 0
passenger_id = 0

# Returns the row and col of the next available seat on the plane (if available)
# ZigZag from front to back, left --> right on even rows, right --> left on odd rows
# The ZigZag makes the algorithm just slightly less dicky
def next_available_seat():
  for row in range(0,30):
    # even rows left --> right
    if row % 2 == 0:
      for col in range(0,6):
        if seating_chart[row][col] == -1:
          return row, col
    # odd rows right --> left
    else:
      for col in range(5,-1,-1):
        if seating_chart[row][col] == -1:
          return row, col
  # Return -1, -1 if not found
  return -1, -1
