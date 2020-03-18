#trying_out_decorators

def check_non_negative():
  def validator(f):
    def wrap(*args):
      if args[1] < 0:
        raise ValueError("Argument {} must be positive".format(args[1]))
      return f(*args)
    return wrap
  return validator


@check_non_negative()
def create_list(value, size):
  return [value] * size


a = create_list('a', 3)
print(a)

b = create_list(123, -100)
print(b)
