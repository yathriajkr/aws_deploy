
def validate():
  print("Hello")
  some = "Hello"
  return some


class FilterModule(object):
    def filters(self):
        return {
            'validate': validate
        }

