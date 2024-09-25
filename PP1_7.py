'''
Lesson: 1.7 Booleans
'''



def q1():
  bool1 = True
  print(bool1)


def q2():
  wendy = input("type an integer: ")
  wendy = int(wendy)
  bool1 = wendy > 5
  print(bool1)

def q3():
  weak = input("Input the letter a: ")
  weak = float(weak)
  a = int(weak)
  bool1 = True
  bool1 = weak == a
  print(bool1)


def q4():
  weird = input("Input a word earlier in the dictionary than google: ")
  weird = int(weird)
  bool1 = True
  bool1 = weird > "google" 
  print(bool1)

def q5():
  sean = input("Input an integer: ")
  sean = int(sean)
  den = input("Input another integer: ")
  den = int(den)
  bool1 = True
  
  print("your numbers multiplied together are greater than 40:  ")

  bool1 = {den + sean} > 40

#Do edit the code below
#Comment the lines below when running your tests

q1()
q2()
q3()
q4()
q5()
