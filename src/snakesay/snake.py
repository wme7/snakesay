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

def bubble(message: str) -> str:
    bubble_length = len(message) + 2
    return f""" {"_" * bubble_length}\n( {message} )\n {"‾" * bubble_length}"""

def say(message: str) -> str:
    return f"""{bubble(message)} {SNAKE}"""