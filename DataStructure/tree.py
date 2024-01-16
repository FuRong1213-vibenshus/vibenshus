import turtle

def tree(branchLen,t):
    if branchLen > 10:
        t.forward(branchLen)
        t.right(40)
        tree(branchLen-30,t)
        t.left(80)
        tree(branchLen-30,t)
        t.right(40)
        t.backward(branchLen)

def main():
    myWin = turtle.Screen()
    myWin.bgcolor("black")
    t = turtle.Turtle()    
    t.width(10)
    t.left(90)
    t.up()
    
    t.backward(100)
    t.down()
    t.color("silver")
    tree(150,t)
    myWin.exitonclick()

main()