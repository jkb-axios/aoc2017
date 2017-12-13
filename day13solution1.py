severity = 0
with open('day13input.txt') as f:
  for l in f:
    tmp = l.split(': ')
    if len(tmp) == 2:
      if int(tmp[0])%((int(tmp[1])-1)*2) == 0:
        severity += int(tmp[0])*int(tmp[1])

print severity
