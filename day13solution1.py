severity = 0
with open('day13input.txt') as f:
  for l in f:
    idx,depth = [int(x) for x in l.split(': ')]
    if idx%((depth-1)*2) == 0:
      severity += idx*depth

print severity
