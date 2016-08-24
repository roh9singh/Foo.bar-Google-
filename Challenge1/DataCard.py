#one can also process the return values using datetime()


#from datetime import datetime



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
