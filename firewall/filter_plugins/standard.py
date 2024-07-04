
def validate(hostname):
  print("Hello")
  some = "Hello "+ hostname
  return some


class FilterModule(object):
    def filters(self):
        return {
            'validate': validate
        }

