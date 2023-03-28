# Improved code for a program that moves asterisks back and forth until `Ctrl-C` is pressed
import time
import sys

def animate_asterisks(max_indent=20, sleep_time=0.1):
    indent = 0
    increasing_indent = True

    try:
        while True:
            print(' ' * indent + '********')
            time.sleep(sleep_time)

            if increasing_indent:
                indent += 1
                if indent == max_indent:
                    increasing_indent = False
            else:
                indent -= 1
                if indent == 0:
                    increasing_indent = True
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    animate_asterisks()
