#!/bin/env python

import os, sys, math
from pprint import pprint as pp

def day1a():
  with open('day1input.txt') as f:
    num = f.read().strip()
    return sum([int(num[i]) for i in xrange(len(num)) if num[i] == num[(i+1)%len(num)]])

def day1b():
  with open('day1input.txt') as f:
    num = f.read().strip()
    return sum([int(num[i]) for i in xrange(len(num)) if num[i] == num[(i+(len(num)/2))%len(num)]])

def day2a():
  chksum=None
  with open('day2input.txt') as f:
    diffs = []
    for l in f:
      nmin=None
      nmax=None
      for n in l.split():
        if nmin == None or int(n) < nmin:
          nmin = int(n)
        if nmax == None or int(n) > nmax:
          nmax = int(n)
      #print 'Min',nmin,'Max',nmax
      if nmin != None:
        diffs.append(nmax-nmin)
    chksum = sum(diffs)
  return chksum

def day2b():
  chksum=None
  with open('day2input.txt') as f:
    quots = []
    for l in f:
      num=None
      den=None
      vals = [int(x) for x in l.split()]
      vals.sort(reverse=1)
      for i in xrange(len(vals)-1):
        for x in vals[i+1:]:
          if vals[i]%x == 0:
            num = vals[i]
            den = x
            break;
        if num != None:
          break;
      #print 'Numerator',num,'Denomenator',den
      if num != None:
        quots.append(num/den)
    chksum = sum(quots)
  return chksum

def day3a():
  num = 265149
  # get num of rows/cols for full NxN spiral matrix containing val
  sz = int(math.ceil(math.sqrt(num))/2)*2+1
  dist = int(sz/2) # must be in one of the perimeter segments
  # break perimeter into 4 segments, each including both corners
  # find missing distance using distance from middle of segment
  if num >= (sz**2)-(sz-1):
    # bottom row
    dist += abs(((sz**2)-((sz-1)/2))-num)
  elif num >= (sz**2)-(2*(sz-1)):
    # left column
    dist += abs(((sz**2)-(3*(sz-1)/2))-num)
  elif num >= (sz**2)-(3*(sz-1)):
    # top row
    dist += abs(((sz**2)-(5*(sz-1)/2))-num)
  else:
    # right column
    dist += abs(((sz**2)-(7*(sz-1)/2))-num)
  return dist

def day3b():
  num = 265149
  def sum_adjacent(m, x, y):
    return sum(m[x-1][y-1:y+2]) + sum(m[x][y-1:y+2]) + sum(m[x+1][y-1:y+2])
  # assuming (perhaps incorrectly) that matrix will be smaller than one above
  sz = int(math.ceil(math.sqrt(num))/2)*2+1
  sz+=2 # add perimeter of 0-filled cells
  m = [ [0 for _ in xrange(sz)] for _2 in xrange(sz)]
  o = (sz-1)/2 # origin is (o,o)
  m[o][o] = 1
  val = 1
  x = y = o
  direction = 1 # 0 right, 1 up, 2 left, 3 down
  while val <= num:
    if direction == 0: # right
      x+=1
      val = sum_adjacent(m,x,y)
      m[x][y] = val
      if m[x][y+1] == 0:
        direction = (direction+1)%4
    elif direction == 1: # up
      y+=1
      val = sum_adjacent(m,x,y)
      m[x][y] = val
      if m[x-1][y] == 0:
        direction = (direction+1)%4
    elif direction == 2: # left
      x-=1
      val = sum_adjacent(m,x,y)
      m[x][y] = val
      if m[x][y-1] == 0:
        direction = (direction+1)%4
    else: # direction == 3 # down
      y-=1
      val = sum_adjacent(m,x,y)
      m[x][y] = val
      if m[x+1][y] == 0:
        direction = (direction+1)%4

  return val

def day4a():
  cnt = 0
  with open('day4input.txt') as f:
    for l in f:
      words = l.split()
      unique = set(words)
      if len(words) == len(unique):
        cnt+=1
  return cnt

def day4b():
  def valid(words):
    #words.sort(key=lambda x: len(x))
    l1 = [ ''.join(sorted([x for x in y])) for y in words]
    if len(l1) == len(set(l1)):
      return True
    return False
  cnt = 0
  with open('day4input.txt') as f:
    for l in f:
      words = l.split()
      unique = set(words)
      if len(words) != len(unique):
        continue
      if valid(words):
        cnt+=1
  return cnt


if __name__ == '__main__':
  print 'Day 1 part 1:', day1a()
  print 'Day 1 part 2:', day1b()
  print 'Day 2 part 1:', day2a()
  print 'Day 2 part 2:', day2b()
  print 'Day 3 part 1:', day3a()
  print 'Day 3 part 2:', day3b()
  print 'Day 4 part 1:', day4a()
  print 'Day 4 part 2:', day4b()


