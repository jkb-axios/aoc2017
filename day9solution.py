import re

in9 = ''
with open('day9input.txt') as f:
  in9 = f.read()

# remove cancelled characters
in9 = re.sub(r'!.', '', in9)

# remove garbage
in9 = re.sub(r'<.*?>', '', in9)

# calculate score
value = 1
score = 0
for x in in9:
  if x == '{':
    score += value
    value += 1
  elif x == '}':
    value -= 1
  elif x == ',':
    pass
  else:
    print 'Why is this character in here:',x

print score
