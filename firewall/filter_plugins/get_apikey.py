def keygen(hostname,username,password):
    
    import xmltodict
    from ansible.module_utils.basic import to_text
    from ansible.module_utils.six.moves import urllib
    import requests
    import json

    params = {"type": "keygen", "user": username, "password": password}
    data = urllib.parse.urlencode(params)
    
    url = 'https://{0}/api/?{1}'.format(hostname, data)
    response = requests.get(url, verify=False,)
    data_decode=response.content.decode("utf-8")
    data = json.loads(xmltodict.parse(data_decode))
    # data = json.dumps(xmltodict.parse(response.content))
    # data = json.loads(data)
    print(data)
    print(type(data))
    # xml = fromstring(response.content))
    # data_json = json.dumps(xmljson.badgerfish.data(xml))
    # print(data_json,type(data_json))
    # data = to_text(response.content)
    # root = ET.fromstring(data)
    # print(response.content)
    # print(root.findall("."))
    # print(root.attrib.items())
    # apikey=data["response"]["result"]["key"]
    apikey='dummy'
    return apikey

class FilterModule(object):
    def filters(self):
        return {
            'keygen': keygen
        
        }
