from . import snake


def main(args=None) -> None:
    parsed_args = snake.parse_args(args)
    message = " ".join(parsed_args.message)
    if "cow" in message:
        print(snake.say(message))
        print(snake.cowsay("I'm here Moo!"))
    else:
        print(snake.say(message))


if __name__ == "__main__":
    main()
