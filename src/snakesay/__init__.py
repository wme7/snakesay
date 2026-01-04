from . import snake


def main(args=None) -> None:
    parsed_args = snake.parse_args(args)
    message = " ".join(parsed_args.message)
    print(snake.say(message))


if __name__ == "__main__":
    main()
