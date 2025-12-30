import sys
from . import snake

def main() -> None:
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
    else:
        message = "Hello, World!!!"
    print(snake.say(message))

if __name__ == "__main__": 
    main()
