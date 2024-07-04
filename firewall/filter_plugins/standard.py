def ftr_static_route(device_data):
  print(device_data)
  zones = device_data["ansible_facts"]["ansible_net_virtual-systems"][0]["vsys_zonelist"])
  #for data in device_data:
  
  return device_data

def validate_zones(std_config, device_config):
  print("Hello")
  missing = {}
  temp
  if std_config not in device_config
  
  miss_routes = "Hello "
  return miss_routes


class FilterModule(object):
    def filters(self):
        return {
            'ftr_static': ftr_static_route,
            'validate_static': validate_static
        }
