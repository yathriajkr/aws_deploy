def ftr_servobj(serv_data):
  servobj =  serv_data['objects']
  return servobj

def validate_servobj(std_config, device_config)
  print(device_config
  missing_addrobj = []
  temp = {}
  for servobj in std_config:
    # print("Enter obj")
    print(servobj)
    for dev_servobj in device_config:
      temp = {}
      if servobj["name"] == dev_servobj['name'] and servobj["destination_port"] == dev_servobj['destination_port']:
        # print("found match")
        temp = servobj
        missing_servobj.append(temp)
  print(missing_servobj)
  return missing_servobj


def ftr_addrobj(addr_data):
  addrobj =  addr_data['objects'][0]
  return addrobj

def validate_addrobj(std_config, device_config)
  print(device_config
  missing_addrobj = []
  temp = {}
  for addrobj in std_config:
    # print("Enter obj")
    print(addrobj)
    temp = {}
    if addrobj["name"] not in device_config:
      # print("found match")
      temp = addrobj
      missing_addrobj.append(temp)
  print(missing_addrobj)
  return missing_addrobj


def ftr_zone(device_data):
  # print(device_data)
  zones = device_data["ansible_facts"]["ansible_net_virtual-systems"][0]["vsys_zonelist"]
  #for data in device_data:
  return zones

def validate_zone(std_config, device_config):
  # print(device_config)
  missing_zones = []
  temp = {}
  for zone in std_config:
    # print("Enter zone")
    print(zone)
    temp = {}
    if zone["zone_name"] not in device_config:
      # print("found match")
      temp = zone
      missing_zones.append(temp)
    
  # print(missing_zones)
  return missing_zones

def xml2json(value):
    import xmltodict, json
    return json.dumps(xmltodict.parse(value))

class FilterModule(object):
    def filters(self):
        return {
            'xml2json': xml2json,
            'ftr_zone': ftr_zone,
            'validate_zone': validate_zone,
            'ftr_addrobj': ftr_addrobj,
            'validate_addrobj': validate_addrobj,
            'ftr_servobj': ftr_servobj,
            'validate_servobj': validate_servobj
        }
