#!/usr/bin/env python3
import subprocess, sys, os, json

data=''
path=''
repo=''
plb=''

path=sys.argv[1]+'/'
with open(sys.argv[2]) as json_file:
    data = json.load(json_file)

try: 
    os.chdir(path)
except OSError:
    print("Can't change the Current Working Directory")
    exit(1)

#if vault params present try to pass them to Ansible
if 'vault' in data['params']:
    if 'inventory' in data['params']:
        try:
            os.environ['ANSIBLE_VAULT_PASSWORD'] = data['params']['vault']['secret']
            os.system('/usr/bin/ansible-playbook '+' -i '+data['params']['inventory']+' '+data['params']['playbook']+' '+data['params']['vault']['args'])
        except Exception:
            print('Found vault params but something failed')
            exit(1)
    else:
        try:
            os.environ['ANSIBLE_VAULT_PASSWORD'] = data['params']['vault']['secret']
            os.system('/usr/bin/ansible-playbook '+' -i /dev/null '+data['params']['playbook']+' '+data['params']['vault']['args'])
        except Exception:
            print('Found vault params but something failed')
            exit(1)
else:
    if 'inventory' in data['params']:
        try:
            os.system('/usr/bin/ansible-playbook '+' -i '+data['params']['inventory']+' '+data['params']['playbook'])
        except Exception:
            print('Found vault params but something failed')
            exit(1)
    else:
        os.system('/usr/bin/ansible-playbook '+' -i /dev/null '+data['params']['playbook'])
