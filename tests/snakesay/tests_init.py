from snakesay import snake

BUBBLE_HI = " _____\n( hi! )\n ‾‾‾‾‾"

SNAKE_HI = " _____\n( hi! )\n ‾‾‾‾‾ \n  \\\n   \\    __\n    \\  {oo}\n       (__)\\\n         λ \\\\\n           _\\\\__\n          (_____)_\n         (________)Oo°\n"


def test_generate_list():
    assert 42 == snake.generate_list()


def test_snake_bubble():
    assert BUBBLE_HI == snake.bubble("hi!")


def test_snake_say():
    assert SNAKE_HI == snake.say("hi!")


def test_main():
    from snakesay import main

    main()
