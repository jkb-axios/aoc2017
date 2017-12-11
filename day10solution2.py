
def knot(rope, length, position):
  #print 'position:', position, 'length:', length, 'rope:', rope
  segment1 = rope[position:min(len(rope),position+length)]
  #print 'segment1:', segment1
  segment2 = rope[0:length-len(segment1)]
  #print 'segment2:', segment2
  segment = segment1 + segment2
  #print 'segment:', segment
  segment.reverse()
  #print 'segment:', segment
  segment1 = segment[:len(segment1)]
  #print 'segment1 reversed:', segment1
  segment2 = segment[len(segment1):]
  #print 'segment2 reversed:', segment2
  result = segment2 + rope[len(segment2):position] + segment1 + rope[position+len(segment1):]
  #print 'result:', result
  return result

# test
#print knot([0,1,2,3,4], 3, 0)

rope_len = 256
in10 = ''
with open('day10input.txt') as f:
  in10 = f.read().strip()

# test input
#in10 = 'AoC 2017'
#print len(in10), in10

rope = range(rope_len)
pos = 0
skip = 0
in10 = [ord(x) for x in in10] + [17, 31, 73, 47, 23]

#print len(in10), in10

for _ in xrange(64):
  for l in in10:
    #print 'LENGTH:', l, 'pos:', pos, 'skip:', skip
    if l > len(rope):
      continue
    # reverse the order of length (l) elements, starting at pos
    rope = knot(rope, l, pos)
    # move pos forward by length + skip size (l + skip)
    pos = (pos + l + skip)%len(rope)
    #print 'new position:', pos
    # increase skip size by 1
    skip += 1
    #print 'new skip size:', skip

print 'Sparse Hash:', rope

dense_hash = []
tmp = 0
for i,x in enumerate(rope):
  tmp ^= x
  if i%16 == 15:
    dense_hash.append(tmp)
    tmp = 0

print 'Dense Hash:', dense_hash

dense_hash = ''.join('%02x'%x for x in dense_hash)
print 'Dense Hash:', dense_hash

# 06d33782fb6fb8c42d484b121435a431