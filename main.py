import turtle

def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
      count+=1
      if(n % 2) == 0:        # n is even
        n = n // 2
      else:                 # n is odd
        n = n * 3 + 1
    return count

def lineGraph(uplim):
  screen = turtle.Screen()
  ymax = 0
  for count in range(uplim):
    ynew = seq3np1(count+1)
    if ynew > ymax:
      ymax = ynew
  screen.setworldcoordinates(0,0,uplim + 10, ymax + 2)
  screen.bgcolor("White")
  myturtle = turtle.Turtle()
  myturtle.speed(0)
  myturtle.fillcolor("Red")
  max_so_far = 0
  for start in range (uplim):
    ycoor = seq3np1(start+1)
    if max_so_far < ycoor:
      max_so_far = ycoor
    myturtle.goto(start+1,ycoor)
    result = "Maximum so far: " + str(start+1) + ", " + str(max_so_far)
    print(result)
  screen.exitonclick()

def main():
  uplim = int(input("Please enter the upper bound: "))
  lineGraph(uplim)
  if (uplim>0):
    for start in range (uplim):
      value = int(seq3np1(start+1))
      print("The start value is " + str(start+1) + ", and the number of iterations is " + str(value))
  else:
    print("Invalid value")
main()
