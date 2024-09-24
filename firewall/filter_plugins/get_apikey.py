def keygen(hostname,username,password):
    from ansible.module_utils.six.moves import urllib
    import requests
    import json

    params = {"type": "keygen", "user": username, "password": password}
    data = urllib.parse.urlencode(params)
    
    url = 'https://{0}/api/?{1}'.format(hostname, data)
    response = requests.get(url, verify=False,)
    json_object = json.loads(response.content)
    json_formatted_str = json.dumps(json_object, indent=2)
    print(response.content)
    print(json_formatted_str)
    apikey="dummy"
    return apikey

class FilterModule(object):
    def filters(self):
        return {
            'keygen': keygen
        
        }
