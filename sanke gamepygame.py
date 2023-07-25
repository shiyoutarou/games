import curses
import random
import time

def create_food(snake, window):
    food = None
    while food is None:
        food = (random.randint(1, window[0]-2), random.randint(1, window[1]-2))
        if food in snake:
            food = None
    return food

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(150)

    window = stdscr.getmaxyx()

    snake = [(window[0] // 2, window[1] // 2)]
    direction = curses.KEY_RIGHT

    food = create_food(snake, window)

    while True:
        new_head = (snake[0][0], snake[0][1])
        key = stdscr.getch()

        if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            key = direction

        if key == curses.KEY_RIGHT:
            new_head = (snake[0][0], snake[0][1] + 1)
        elif key == curses.KEY_LEFT:
            new_head = (snake[0][0], snake[0][1] - 1)
        elif key == curses.KEY_UP:
            new_head = (snake[0][0] - 1, snake[0][1])
        elif key == curses.KEY_DOWN:
            new_head = (snake[0][0] + 1, snake[0][1])

        snake.insert(0, new_head)

        if snake[0] == food:
            food = create_food(snake, window)
        else:
            snake.pop()

        stdscr.clear()
        for y, x in snake:
            stdscr.addch(y, x, "#")

        stdscr.addch(food[0], food[1], "*")

        if (snake[0][0] in [0, window[0]-1] or
            snake[0][1] in [0, window[1]-1] or
            snake[0] in snake[1:]):
            stdscr.addstr(window[0] // 2, window[1] // 2, "Game Over", curses.A_BOLD)
            stdscr.refresh()
            time.sleep(2)
            break

        stdscr.refresh()
        direction = key

if __name__ == "__main__":
    curses.wrapper(main)
