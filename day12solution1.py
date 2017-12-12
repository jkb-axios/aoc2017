mapping = {}

with open('day12input.txt') as f:
  for l in f:
    tmp = l.split()
    if len(tmp) == 0:
      continue
    lhs = int(tmp[0])
    rhs = [int(x.strip(',')) for x in tmp[2:] ]
    mapping[lhs] = rhs

group = []
new_grp = [0]
while len(new_grp) > 0:
  x = new_grp.pop(0)
  if x not in group:
    group.append(x)
    new_grp.extend([y for y in mapping[x] if y not in group+new_grp])

print len(group)
