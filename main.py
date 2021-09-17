# Let’s break the code down into smaller chunks to help fix the logic errors.
# Follow the instructions here to complete the task: https://education.launchcode.org/data-analysis/chapters/errors-and-debugging/studio.html#solve-logic-errors-last

launch_ready = False
fuel_level = 17000
crew_status = True
computer_status = 'green'

if fuel_level >= 20000:
  print('Fuel level cleared.')
  launch_ready = True
else:
  print('WARNING: Insufficient fuel!')
  launch_ready = False

if crew_status and computer_status == 'green':
  print('Crew & computer cleared.')
  launch_ready = True
else:
  print('WARNING: Crew or computer not ready!')
  launch_ready = False

if launch_ready:
  print('10, 9, 8, 7, 6, 5, 4, 3, 2, 1...')
  print('Liftoff!')
else:
  print('Launch scrubbed.')
