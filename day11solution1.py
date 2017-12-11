in11 = ''
with open('day11input.txt') as f:
  in11 = f.read().strip()

# test input
#in11 = 'ne,ne,ne'
#in11 = 'ne,ne,sw,sw'
#in11 = 'ne,ne,s,s'
#in11 = 'se,sw,se,sw,sw'

in11 = in11.split(',')

num_se = in11.count('se')
num_sw = in11.count('sw')
num_ne = in11.count('ne')
num_nw = in11.count('nw')
num_s = in11.count('s')
num_n = in11.count('n')
#print 'n: ', num_n
#print 'ne:', num_ne
#print 'se:', num_se
#print 's: ', num_s
#print 'sw:', num_sw
#print 'nw:', num_nw

# totals for the 3 directions we can move
total_n = num_n - num_s
total_ne = num_ne - num_sw
total_nw = num_nw - num_se
#print 'total n: ', total_n
#print 'total ne:', total_ne
#print 'total nw:', total_nw

# look at grid as normal square grid by ignoring every other column
# - each 2 steps NE = 1 north and 1 east
# - each 2 steps NW = 1 north and 1 west
# - each E step is really 2 steps, and can also move 1 N or S for free
# - have to account for the potential odd number of ne and nw steps

total_n_steps = total_n + int(float(total_ne)/2) + int(float(total_nw)/2)
total_e_steps = int(float(total_ne)/2) - int(float(total_nw)/2)
#print 'total n steps:', total_n_steps
#print 'total e steps:', total_e_steps

total_steps = abs(2*total_e_steps) + max(0,abs(total_n_steps)-abs(total_e_steps))
if total_ne%2 or total_nw%2:
  #print 'adding 1 odd step'
  total_steps += 1

print 'total steps:', total_steps

