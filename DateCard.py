'''

Origins and order
=================

What do we know about Professor Boolean's past? It's mostly rumor and conjecture, but a few things are known to be true.

Mad Professor Boolean wasn't always a super villain. Early in his career, he was an average paper pusher, working in an office with some very backwards technology. 
One of his primary jobs was to carry date cards between departments. One morning, he tripped over a unicycle and dropped his date cards on the floor. 
He hit his head - and hit upon the idea of breeding an army of zombie rabbits to do his bidding and manage simple tasks. But that comes later. 
Before he could quit with an explosive YouTube video, the professor had to get his cards back in order.

Aha! It seems he recorded the details of this life-changing event in his diary. Let's try to reproduce his methods:

The goal is to get the date cards back in order. Each set of date cards consists of 3 cards, each with a number written on it. 
When arranged in some order, the numbers make up the representation of a date, in the form month/day/year. However, sometimes multiple 
representations will be possible. For example, if the date cards read 1, 1, 99 it could only mean 01/01/99, but if the date cards read 2, 30, 3, 
it could mean any one of 02/03/30, 03/02/30, or 03/30/02.

Write a function called answer(x, y, z) that takes as input the 3 numbers on the date cards. You may assume that at least one valid representation of 
a date can be constructed from the cards.

If there is only one valid representation, the function should return it as a string, in the form MM/DD/YY. If there are multiple valid representations, 
the function should return the string "Ambiguous." Each of x, y, z will be between 1 to 99 inclusive. You may also assume that there are no leap years.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) x = 19
    (int) y = 19
    (int) z = 3
Output:
    (string) "03/19/19"

Inputs:
    (int) x = 2
    (int) y = 30
    (int) z = 3
Output:
    (string) "Ambiguous"

Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. 
If your solution passes the test cases, it will be removed from your home folder.
'''



from datetime import datetime



def MonthDay(a,b):
 if a==b and a<=12 and b<=12:
  return [a,b]
 elif(a<=12 and b>12):
  return [a,b]			#month then Day
 elif (a>12 and b<=12):
  return [b,a]
 else:
  return -1



def YearDay(a,b):
 if a==b and a<=31 and b<=31:
  return [a,b]
 elif(a<=31 and b>31):
  return [a,b]			#Day then Year
 elif(a>=31 and b<=31):
  return [b,a]
 else:
  return -1


def validMD(a,b,c):

 if (a==2 and (b==29 or b==30 or b==31)) or (a==4 and b==31) or (a==6 and b==31) or (a==9 and b==31) or (a==11 and b==31):
  return -1
 else: 
  return 1 
  
  

def answer(x, y, z):
 A="Ambiguous"
 x=int(x)
 y=int(y)
 z=int(z)
 Cards=[int(x),int(y),int(z)]
 
 if any(True if i > 31 else False for i in Cards):
  if x>31:
   t=MonthDay(y,z)
   c=x
  elif y>31:
   t=MonthDay(x,z)
   c=y
  elif z>31:
   t=MonthDay(x,y)
   c=z
  else:
   t=-1
  
  if t==-1:
   return A
  else:
   t.append(c)
  
   
 else:
  if x==y and x==z and y==z and sum([True if i <= 12 else False for i in Cards])==3:
   c=x
   t=[y,z]
  elif sum([True if i <= 12 else False for i in Cards])>1:
   t=-1
  else:
   if x<=12:
    c=x
    t=YearDay(y,z)
   elif y<=12:
    c=y
    t=YearDay(x,z)
   elif z<=12:
    c=z
    t=YearDay(x,y)
   else:
    t=-1
  
  if t==-1:
   return A
  else:
   t.insert(0,c)
 
 
 
 if validMD(t[0],t[1],t[2])==-1:
  return A   
  #dt = datetime(year=t[2]+2000, month=t[1], day=t[0])
  #date=dt.strftime('%m/%d/%y')
 date=""
 for i in t:
  if i<10:
   date+="0"+str(i)+"/"
  else:
   date+=str(i)+"/"	
 return date[0:8]





print(answer((input("X")),(input("Y")),(input("Z"))))