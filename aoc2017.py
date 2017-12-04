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
  x = y = (sz-1)/2 # this is the origin
  m[x][y] = val = 1
  direction = 1 # 0 right, 1 up, 2 left, 3 down
  # start with "up" which visually is "right" if matrix is printed
  # b/c my matrix is list(y) of lists(x), x/y are flipped
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

def day5a():
  pass

def day5b():
  pass

def day6a():
  pass

def day6b():
  pass

def day7a():
  pass

def day7b():
  pass

def day8a():
  pass

def day8b():
  pass

def day9a():
  pass

def day9b():
  pass

def day10a():
  pass

def day10b():
  pass

def day11a():
  pass

def day11b():
  pass

def day12a():
  pass

def day12b():
  pass

def day13a():
  pass

def day13b():
  pass

def day14a():
  pass

def day14b():
  pass

def day15a():
  pass

def day15b():
  pass

def day16a():
  pass

def day16b():
  pass

def day17a():
  pass

def day17b():
  pass

def day18a():
  pass

def day18b():
  pass

def day19a():
  pass

def day19b():
  pass

def day20a():
  pass

def day20b():
  pass

def day21a():
  pass

def day21b():
  pass

def day22a():
  pass

def day22b():
  pass

def day23a():
  pass

def day23b():
  pass

def day24a():
  pass

def day24b():
  pass

def day25a():
  pass

def day25b():
  pass

if __name__ == '__main__':
  run = []
  #run = [1,2,3,4]
  #run = [5]
  if not run or 1 in run: print 'Day 1  Part 1:', day1a()
  if not run or 1 in run: print 'Day 1  Part 2:', day1b()
  if not run or 2 in run: print 'Day 2  Part 1:', day2a()
  if not run or 2 in run: print 'Day 2  Part 2:', day2b()
  if not run or 3 in run: print 'Day 3  Part 1:', day3a()
  if not run or 3 in run: print 'Day 3  Part 2:', day3b()
  if not run or 4 in run: print 'Day 4  Part 1:', day4a()
  if not run or 4 in run: print 'Day 4  Part 2:', day4b()
  if not run or 5 in run: print 'Day 5  Part 1:', day5a()
  if not run or 5 in run: print 'Day 5  Part 2:', day5b()
  if not run or 6 in run: print 'Day 6  Part 1:', day6a()
  if not run or 6 in run: print 'Day 6  Part 2:', day6b()
  if not run or 7 in run: print 'Day 7  Part 1:', day7a()
  if not run or 7 in run: print 'Day 7  Part 2:', day7b()
  if not run or 8 in run: print 'Day 8  Part 1:', day8a()
  if not run or 8 in run: print 'Day 8  Part 2:', day8b()
  if not run or 9 in run: print 'Day 9  Part 1:', day9a()
  if not run or 9 in run: print 'Day 9  Part 2:', day9b()
  if not run or 10 in run: print 'Day 10 Part 1:', day10a()
  if not run or 10 in run: print 'Day 10 Part 2:', day10b()
  if not run or 11 in run: print 'Day 11 Part 1:', day11a()
  if not run or 11 in run: print 'Day 11 Part 2:', day11b()
  if not run or 12 in run: print 'Day 12 Part 1:', day12a()
  if not run or 12 in run: print 'Day 12 Part 2:', day12b()
  if not run or 13 in run: print 'Day 13 Part 1:', day13a()
  if not run or 13 in run: print 'Day 13 Part 2:', day13b()
  if not run or 14 in run: print 'Day 14 Part 1:', day14a()
  if not run or 14 in run: print 'Day 14 Part 2:', day14b()
  if not run or 15 in run: print 'Day 15 Part 1:', day15a()
  if not run or 15 in run: print 'Day 15 Part 2:', day15b()
  if not run or 16 in run: print 'Day 16 Part 1:', day16a()
  if not run or 16 in run: print 'Day 16 Part 2:', day16b()
  if not run or 17 in run: print 'Day 17 Part 1:', day17a()
  if not run or 17 in run: print 'Day 17 Part 2:', day17b()
  if not run or 18 in run: print 'Day 18 Part 1:', day18a()
  if not run or 18 in run: print 'Day 18 Part 2:', day18b()
  if not run or 19 in run: print 'Day 19 Part 1:', day19a()
  if not run or 19 in run: print 'Day 19 Part 2:', day19b()
  if not run or 20 in run: print 'Day 20 Part 1:', day20a()
  if not run or 20 in run: print 'Day 20 Part 2:', day20b()
  if not run or 21 in run: print 'Day 21 Part 1:', day21a()
  if not run or 21 in run: print 'Day 21 Part 2:', day21b()
  if not run or 22 in run: print 'Day 22 Part 1:', day22a()
  if not run or 22 in run: print 'Day 22 Part 2:', day22b()
  if not run or 23 in run: print 'Day 23 Part 1:', day23a()
  if not run or 23 in run: print 'Day 23 Part 2:', day23b()
  if not run or 24 in run: print 'Day 24 Part 1:', day24a()
  if not run or 24 in run: print 'Day 24 Part 2:', day24b()
  if not run or 25 in run: print 'Day 25 Part 1:', day25a()
  if not run or 25 in run: print 'Day 25 Part 2:', day25b()

