def keygen(hostname,username,password):
    
    import xml.etree.ElementTree as ET
    from ansible.module_utils.basic import to_text
    from ansible.module_utils.six.moves import urllib
    import requests
    import json

    params = {"type": "keygen", "user": username, "password": password}
    data = urllib.parse.urlencode(params)
    
    url = 'https://{0}/api/?{1}'.format(hostname, data)
    response = requests.get(url, verify=False,)
    data = to_text(response.content)
    root = ET.fromstring(data)
    print(response.content)
    print(root.attrib)
    apikey="dummy"
    return apikey

class FilterModule(object):
    def filters(self):
        return {
            'keygen': keygen
        
        }
