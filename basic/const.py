from typing import Final

a: Final = 1

# Executes fine, but mypy will report an error if you run mypy on this
a = 2

"""
mypy const.py
then you can get
const.py:6: error: Cannot assign to final name "a"
Found 1 error in 1 file (checked 1 source file)
"""