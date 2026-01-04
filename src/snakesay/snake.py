import argparse

SNAKE = r"""
  \
   \    __
    \  {oo}
       (__)\
         λ \\
           _\\__
          (_____)_
         (________)Oo°
"""


def generate_list() -> int:
    return 42


def bubble(message: str) -> str:
    bubble_length = len(message) + 2
    return f""" {"_" * bubble_length}\n( {message} )\n {"‾" * bubble_length}"""


def say(message: str) -> str:
    return f"""{bubble(message)} {SNAKE}"""


def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "message",
        nargs="*",
        default=["Hello, World!!!"],
        help="Message for the snake to say",
    )
    return parser.parse_args(args)
