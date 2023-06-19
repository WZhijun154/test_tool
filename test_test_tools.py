
from test_tool import TestTool, Context

@TestTool.test_args(is_testing = True)(1,2)
def add(x,y):
   print(f"{x} + {y} = {x+y}")

@TestTool.test_args(is_testing = True)("Alice", "Bob")
def greet(*names):
   print(f"Hello {', '.join(names)}")


@TestTool.test_context(is_testing = True)(func = add, x = 1, y = 2)
class NormalContext(Context):

   def __init__(self, func, *args, **kwargs):
      self.func = func
      self.args = args
      self.kwargs = kwargs

   def execute(self):
      self.func(*self.args, **self.kwargs)



if __name__ == "__main__":
   TestTool.main()