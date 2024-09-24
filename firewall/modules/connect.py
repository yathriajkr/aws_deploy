#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

import requests
import json


requests.packages.urllib3.disable_warnings()



def connect():

def main():
  module_args = dict(
        hostname=dict(type='str', required=True),
        username=dict(type='str', required=True),
        password=dict(type='str', required=True)
    )
  
  result = dict(
        changed=False,
        message=''
    )

   module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
  print(module.params['hostname']

  module.exit_json(**result)

if __name__ == '__main__':
    main()
  
