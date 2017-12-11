in11 = ''
with open('day11input.txt') as f:
  in11 = f.read().strip()

in11 = in11.split(',')
num_se = 0
num_sw = 0
num_ne = 0
num_nw = 0
num_s = 0
num_n = 0
most_steps = 0

for x in in11:
  if x == 'se': num_se += 1
  elif x == 'sw': num_sw += 1
  elif x == 'ne': num_ne += 1
  elif x == 'nw': num_nw += 1
  elif x == 'n': num_n += 1
  elif x == 's': num_s += 1
  total_n = num_n - num_s
  total_ne = num_ne - num_sw
  total_nw = num_nw - num_se
  total_n_steps = total_n + int(float(total_ne+total_nw)/2)
  total_e_steps = int(float(total_ne-total_nw)/2)
  total_steps = abs(2*total_e_steps) + max(0,abs(total_n_steps)-abs(total_e_steps))
  if total_ne%2 != total_nw%2: total_steps += 1
  most_steps = max(most_steps,total_steps)

print 'most steps:', most_steps
