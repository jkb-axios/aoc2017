grid= []
with open('day13input.txt') as f:
  for l in f:
    tmp = l.split(': ')
    if len(tmp) != 2:
      continue
    grid.append(int(x) for x in tmp)

severity = 0
for idx,depth in grid:
  if idx%((depth-1)*2) == 0:
    severity += idx*depth

print severity