from turtle import *
import random
import turtle as tur
tur.Screen().bgcolor("light blue")

secret_number = 0
row_value=0
radius=10

gummies = 0
number_of_blocks=0

num = [0, 1, 2, 3, 4, 5, 6, 7]
num_blocks = random.choice(num)
number_of_blocks=num_blocks
gummies=number_of_blocks

'''
# to debug
print("secret_number: " + str(secret_number))
print("num_blocks  " + str(num_blocks))
print("gummies: " + str(gummies))
print("number_of_blocks: " + str(number_of_blocks))
'''

colors = ["red", "yellow", "pink", "blue", "purple", "orange"]
selected_color = random.choice(colors)

def jar():
  penup()
  setposition(-75, 75)
  pendown()
  right(90)
  forward(150)
  for i in range(2):
    left(90)
    forward(150)
  right(90)
  
  
def draw_check():
    clear()
    penup()
    setposition(0,0)
    pendown()
    pensize(5)
    color("green")
    left(135)
    forward(50)
    backward(50)
    right(90)
    forward(100)
    right(45)

def up_arrow():
    clear()
    penup()
    setposition(0,0)
    pendown()
    pensize(5)
    left(90)
    forward(100)
    right(135)
    forward(50)
    backward(50)
    left(270)
    forward(50)
    left(135)
    
def down_arrow():
    clear()
    penup()
    setposition(0,0)
    pendown()
    pensize(5)
    right(90)
    forward(100)
    right(135)
    forward(50)
    backward(50)
    left(270)
    forward(50)
    right(45)
   
def move_to_row(gummies):
    x_value = -((gummies*20)/2)
    y_value = -75+(20*row_value)
    penup()
    setposition(x_value,y_value)
    pendown()
  
def draw_block_row(gummies):
    for i in range(gummies):
      color(random.choice(colors))
      begin_fill()
      circle(radius)
      end_fill()
      penup()
      forward(20)
      pendown()
    
# debug statement
# print(num_blocks)


# Draw the jar at a given speed
speed(5)
jar()
speed(0)

#Fill the jar with Gumballs
for i in range(number_of_blocks):
  move_to_row(number_of_blocks)
  row_value=row_value+1
  draw_block_row(number_of_blocks)
  number_of_blocks=number_of_blocks-1


if num_blocks == 0:
  secret_number = 0
elif num_blocks == 1:
  secret_number = 1
elif num_blocks == 2:
  secret_number = 3
elif num_blocks == 3:
  secret_number = 6
elif num_blocks == 4:
  secret_number = 10
elif num_blocks == 5:
  secret_number = 15
elif num_blocks == 6:
  secret_number = 21
elif num_blocks == 7:
  secret_number = 28

'''
# to debug
print("secret_number: " + str(secret_number))
print("num_blocks  " + str(num_blocks))
print("gummies: " + str(gummies))
print("number_of_blocks: " + str(number_of_blocks))
'''


user_number = int(input("How many Gumballs are in the jar? "))
if user_number > secret_number:
  down_arrow()
elif user_number < secret_number:
  up_arrow()
else:
  draw_check()

while user_number != secret_number:
  user_number = int(input("Keep guessing the number of gumballs "))
  if user_number > secret_number:
    down_arrow()
  elif user_number < secret_number:
    up_arrow()
  else:
    draw_check()

