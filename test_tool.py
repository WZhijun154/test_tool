

from abc import abstractmethod, ABCMeta   

class TestTool:
   
   func_tests = []
   context_tests = []

   @staticmethod
   def test_args(is_testing : bool = True):
      def args_wrapper(*args, **kwargs):
         def func_wrapper(func : callable):
            if is_testing:
               TestTool.func_tests.append((func, args, kwargs))
            return func
         return func_wrapper
      return args_wrapper
   
   @staticmethod
   def test_context(is_testing : bool = True):
      def args_wrapper(*args, **kwargs):
         def context_wrapper(context : Context):
            if is_testing:
               TestTool.context_tests.append((context, args, kwargs))
            return context
         return context_wrapper
      return args_wrapper


   @staticmethod
   def main():
      for func, args, kwargs in TestTool.func_tests:
         try:
            func(*args, **kwargs)
         except Exception as e:
            print(f"Test failed: {func.__name__}")
            print(f"Error: {e}")

      for context, args, kwargs in TestTool.context_tests:
         try:
            context(*args, **kwargs).execute()
         except Exception as e:
            print(f"Test failed: {context.__name__}")
            print(f"Error: {e}")


class Context(metaclass = ABCMeta):
   @abstractmethod
   def execute(self): 
      pass



            

      

