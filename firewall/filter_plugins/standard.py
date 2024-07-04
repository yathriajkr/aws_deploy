
def validate(std_config, device_config):
  print("Hello")
  some = "Hello "+ hostname
  return some


class FilterModule(object):
    def filters(self):
        return {
            'validate': validate
        }

