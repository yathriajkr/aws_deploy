def ftr_zone(device_data):
  print(device_data)
  # zones = device_data["ansible_facts"]["ansible_net_virtual-systems"][0]["vsys_zonelist"])
  #for data in device_data:
  zones = ['hello]
  return zones

def validate_zone(std_config, device_config):
  print("Hello")
  missing_zones = []
  temp = {}
  for zone in std_config:
    temp = {}
    if zone.zone_name not in device_config:
      temp = zone
    missing_zones.append(temp)
    
  print(missing_zones)
  return missing_zones

class FilterModule(object):
    def filters(self):
        return {
            'ftr_zone': ftr_zone,
            'validate_zone': validate_zone
        }
