import sys
import select
import tty
import termios
import atexit
def kbhit():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

# old_settings = termios.tcgetattr(sys.stdin)
# def reset_settings():
#     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
#
# tty.setcbreak(sys.stdin.fileno())
# atexit.register(reset_settings)

def getch():
    return sys.stdin.read(1)