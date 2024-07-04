def ftr_zone(device_data):
  print(device_data)
  zones = device_data["ansible_facts"]["ansible_net_virtual-systems"][0]["vsys_zonelist"]
  #for data in device_data:
  return zones

def validate_zone(std_config, device_config):
  print(device_config)
  print("Hello")
  missing_zones = []
  temp = {}
  for zone in std_config:
    print("Enter zone")
    print(zone)
    temp = {}
    if zone["zone_name"] not in device_config:
      print("found match")
      temp = zone
      missing_zones.append(temp)
    
  print(missing_zones)
  return missing_zones

def xml2json(value):
    import xmltodict, json
    return json.dumps(xmltodict.parse(value))

class FilterModule(object):
    def filters(self):
        return {
            'xml2json': xml2json,
            'ftr_zone': ftr_zone,
            'validate_zone': validate_zone
        }
