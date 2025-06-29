import curses


def screen() -> None:
    stdscr = curses.initscr()
    try:
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        win = curses.newwin(curses.LINES // 2, curses.COLS // 2,
                            curses.LINES // 2, curses.COLS // 2)
        win.clear()
        win.addstr(0, 0, "hello world")
        win.refresh()
        win.getch()
    finally:
        curses.nocbreak()
        curses.echo()
        stdscr.keypad(False)
        curses.endwin()


screen()
