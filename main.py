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
  """
  Displays a graph of the input value with it's respective 3n+1 y value. Also displays the max so far.
  args: uplim (int) upper limit of graph
  return: none
  """
  screen = turtle.Screen()
  screen.setworldcoordinates(0,0,10,10)
  screen.bgcolor("White")
  myturtle = turtle.Turtle()
  myturtle.speed(0)
  myturtle.fillcolor("Red")
  max_so_far = 0
  max_turtle = turtle.Turtle()
  max_turtle.up()
  for start in range (uplim):
    screen.setworldcoordinates(0,0,start + 10, max_so_far + 10)
    max_turtle.goto(0, max_so_far)
    max_turtle.write(str(max_so_far))
    ycoor = seq3np1(start+1)
    if max_so_far < ycoor:
      max_so_far = ycoor
    myturtle.goto(start+1,ycoor)
    result = "Maximum so far: " + str(start+1) + ", " + str(max_so_far)
    print(result)
  screen.exitonclick()

def main():
  uplim = int(input("Please enter the upper bound: "))
  if (uplim>0):
    lineGraph(uplim)
    for start in range (uplim):
      value = int(seq3np1(start+1))
      print("The start value is " + str(start+1) + ", and the number of iterations is " + str(value))
  else:
    print("Invalid value")
main()
