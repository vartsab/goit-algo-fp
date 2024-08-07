import turtle
import math

def draw_pythagoras_tree(branch_length, angle, level):
    if level == 0:
        return

    # Малюємо поточну гілку
    turtle.forward(branch_length)

    # Зберігаємо поточну позицію та кут
    position = turtle.position()
    heading = turtle.heading()

    # Малюємо праву гілку
    turtle.left(angle)
    draw_pythagoras_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

    # Відновлюємо збережену позицію та кут
    turtle.setposition(position)
    turtle.setheading(heading)

    # Малюємо ліву гілку
    turtle.right(angle)
    draw_pythagoras_tree(branch_length * math.cos(math.radians(angle)), angle, level - 1)

    # Повертаємося до початкової позиції
    turtle.setposition(position)
    turtle.setheading(heading)

def main():
    # Ініціалізація черепашки
    turtle.bgcolor("black")
    turtle.color("cyan")
    turtle.pencolor("cyan")
    turtle.pensize(7)
    turtle.speed('fastest')
    turtle.left(90)  # Повертаємо черепашку вверх
    turtle.up()
    turtle.goto(0, -250)
    turtle.down()

    # Запитуємо користувача про рівень рекурсії
    level = int(input("Enter the level of recursion: "))

    # Малюємо дерево
    draw_pythagoras_tree(100, 45, level)

    # Завершення
    turtle.done()

if __name__ == "__main__":
    main()
    