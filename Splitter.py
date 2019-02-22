#!/usr/bin/env python
from __future__ import print_function
import webbrowser
x = 1
while x == 1:

 word = ""
 ##winning string
 hope = "048118404998900227311912184555554555555413191586293088565284601612725455555445555511820455544445555555169110095011091071529212914554554455554555172091509325719951371"
 print ("Please say:" + hope)
  
  
 
 ##raw input
 word = raw_input("Give me an input:")
 
 
 
 ag = []
 ##puts every character in ag array
 ag.extend(word)
 ag = ag[:-1]
 ##function prints every other character and then prints the ones it didn't print
 def splitter(ary):
   split = ary[1::2] + ary[0::2]
   return split
   
 ag = (splitter(ag))
 ##append the value of i raised to the third power
 for i in range(len(ag)):
     tow = ag
     ag.append((str(pow(i,3))))
 ##runs spitter function
 ag = splitter(tow)
 tow = ""
 ##puts ag as a string in tow
 for i in range(len(ag)):
     tow += ag[i]
 
 poop = []
 poop.extend(tow)
 
 runescape = []
 ##appends the decimal value of poop array to runescape array
 for i in range(len(poop)):
     runescape.append(ord(str(poop[i])))
  
 
 lastone = []
 lastone.extend(runescape)
 ##runs splitter function on lastone array and sets = to runescape
 runescape = splitter(lastone)
 
 lel = ""
 for i in range(len(runescape)):
     lel += str(runescape[i])
 ##sets runescape equal to spitter function on lel
 runescape = splitter(lel)
 ##winning function prints "this one was easy" and opens a webpage
 def gj():
   print("This one was easy")
   webbrowser.open('https://www.youtube.com/watch?v=mtLpZWNyM0I') 
 
 
 
 ##losing function prints you failed
 def bj():
   print("You Failed!")
 
  
 
 
 
 ## if statement that decides which function to run
 if runescape == hope:
   gj()
   x = 2
 else:
   bj()

