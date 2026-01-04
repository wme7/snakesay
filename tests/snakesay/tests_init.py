from snakesay import snake, main

BUBBLE_HI = " _____\n( hi! )\n ‾‾‾‾‾"

SNAKE_HI = " _____\n( hi! )\n ‾‾‾‾‾ \n  \\\n   \\    __\n    \\  {oo}\n       (__)\\\n         λ \\\\\n           _\\\\__\n          (_____)_\n         (________)Oo°\n"

COW_HI = " _____\n( hi! )\n ‾‾‾‾‾ \n  \\   ^__^\n   \\  (oo)\\_______\n      (__)\\       )\\/\\\n          ||----w |\n          ||     ||\n"


def test_generate_val():
    assert 42 == snake.generate_val()


def test_snake_bubble():
    assert BUBBLE_HI == snake.bubble("hi!")


def test_snake_say():
    assert SNAKE_HI == snake.say("hi!")


def test_cow_say():
    assert COW_HI == snake.cowsay("hi!")


def test_parser():
    args = snake.parse_args(["yum!"])
    assert args.message == ["yum!"]


def test_main_v1():
    main(["Hello, little human-cub!"])


def test_main_v2():
    main(["cow, where are you?"])
