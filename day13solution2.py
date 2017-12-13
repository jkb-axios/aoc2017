grid= []
with open('day13input.txt') as f:
  for l in f:
    tmp = l.split(': ')
    if len(tmp) != 2:
      continue
    grid.append([int(x) for x in tmp])

delay = 0
while 1:
  delay += 1
  for idx,depth in grid:
    if (idx+delay)%((depth-1)*2) == 0:
      break
  else:
    break

print delay