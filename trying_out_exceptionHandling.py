# trying_out_exceptionHandling

import sys

try:
  x = "hello"
  y = x / 2
  print(y)

except (ValueError, TypeError, ZeroDivisionError) as e:
  error_message = e.__traceback__
  print(error_message.print_tb())
