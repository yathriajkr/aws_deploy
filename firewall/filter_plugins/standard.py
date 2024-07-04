def ftr_static_route(device_data):
  print(device_data)
  print(device_data["ansible_facts"]["ansible_net_virtual-systems"][0]["vsys_iflist"])
  #for data in device_data:

  return device_data

def validate_static(std_config, device_config):
  print("Hello")
  
  miss_routes = "Hello "
  return miss_routes


class FilterModule(object):
    def filters(self):
        return {
            'ftr_static': ftr_static_route,
            'validate_static': validate_static
        }
