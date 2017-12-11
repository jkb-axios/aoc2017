import re

in9 = ''
with open('day9input.txt') as f:
  in9 = f.read()

orig_len = len(in9)
print 'orig len is', orig_len

# remove cancelled characters
in9 = re.sub(r'!.', '', in9)
len_wo_cancelled = len(in9)

# make sure key is unique
key = 'kippik'
while in9.count(key) !=0:
  key = 'a'+key+'a'

print 'Key is:', key
len_of_key = len(key)

# replace garbage with key
in9 = re.sub(r'<.*?>', key, in9)
len_w_key = len(in9)
cnt_of_key = in9.count(key)

# remove keys now
in9 = re.sub(key, '', in9)
len_wo_garbage = len(in9)

cnt = len_wo_cancelled - len_wo_garbage - 2*cnt_of_key
print cnt
