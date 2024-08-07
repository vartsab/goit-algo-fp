import turtle
import math

def draw_pythagoras_tree(branch_length, angle, level):
    if level == 0:
        return

    # Draw the current branch
    turtle.forward(branch_length)

    # Save the current position and angle
    position = turtle.position()
    heading = turtle.heading()

    # Draw the right branch
    turtle.left(angle)
    draw_pythagoras_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

    # Restore the saved position and angle
    turtle.setposition(position)
    turtle.setheading(heading)

    # Draw the left branch
    turtle.right(angle)
    draw_pythagoras_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

    # Go back to the initial position
    turtle.setposition(position)
    turtle.setheading(heading)

def main():
    # Initialize turtle
    turtle.bgcolor("black")
    turtle.speed('fastest')
    turtle.left(90)  # Point the turtle upwards
    turtle.up()
    turtle.goto(0, -250)
    turtle.down()
    turtle.color("cyan")
    turtle.pencolor("cyan")
    turtle.pensize(7)

    # Ask user for the recursion level
    level = int(input("Enter the level of recursion: "))

    # Draw the tree
    draw_pythagoras_tree(100, 45, level)

    # Finish
    turtle.done()

if __name__ == "__main__":
    main()
