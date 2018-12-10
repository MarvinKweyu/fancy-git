import os
from blessings import Terminal # $ pip install blessings

full_path = os.getcwd()

t = Terminal()
with t.location(0, t.height - 1):
    print(full_path)