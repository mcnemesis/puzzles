#!/usr/bin/env python
'''
http://www.mindcipher.com/puzzles/120
------
There are 100 light switches, all of them are off. First, you walk by them, turning all of them on. Next, you walk by them turning every other one off. Then, you walk by them changing every third one. On your 4th pass, you change every 4th one.

You repeat this for 100 passes. At the end, how many lights will be on?
--------
ANS : 10 Bulbs
'''

bulbs = [{'on':False,'i':i} for i in xrange(100)]

turnOFF = lambda b: b.update({'on': False})
turnON = lambda b: b.update({'on': True})
toggleSTATE = lambda b: b.update({'on': not b['on']})

def countOn(bulbs):
    print "%d Bulbs ON" % map(lambda b:b['on'],bulbs).count(True)

countOn(bulbs)
map(turnON,bulbs)
countOn(bulbs)
map(lambda b : turnOFF(b) if bulbs.index(b) % 2 == 0  else None, bulbs)
countOn(bulbs)
[ map(lambda b : toggleSTATE(b) if bulbs.index(b) % i == 0  else None, bulbs) for i in xrange(3,100)]
countOn(bulbs)
