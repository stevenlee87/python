import sys
import requests
import json
# import math
# import time
__author__ = "Steven Lee"

# marathon_address = input("Enter the DNS hostname or IP of your Marathon Instance : ")

# max_mem_percent = int(input("Enter the Max percent of Mem Usage averaged across all Application Instances to trigger Autoscale (ie. 80) : "))
# max_cpu_time = int(input("Enter the Max percent of CPU Usage averaged across all Application Instances to trigger Autoscale (ie. 80) : "))
# trigger_mode = input("Enter which metric(s) to trigger Autoscale ('and', 'or') : ")
# autoscale_multiplier = float(input("Enter Autoscale multiplier for triggered Autoscale (ie 1.5) : "))
# max_instances = int(input("Enter the Max instances that should ever exist for this application (ie. 20) : "))
# userid = input('Enter the username for the marathon UI : ')
# password = input('Enter the password for the marathon UI : ')
# marathon_app = input("Enter the Marathon Application Name to Configure Autoscale for from the Marathon UI : ")

# max_mem_percent = 40
# max_cpu_time = 40
# trigger_mode = 'or'
# max_instances = 10
# autoscale_multiplier=4


class Marathon(object):
    def __init__(self, marathon_address, dcos_auth_token):
        self.name = marathon_address
        self.uri = marathon_address
        if dcos_auth_token is not None:
            self.headers = {'Authorization': 'token=' + dcos_auth_token, 'Content-type': 'application/json'}
        else:
            self.headers = {'Content-type': 'application/json'}
        self.apps = self.get_all_apps()

    def get_all_apps(self):
        response = requests.get(self.uri + '/v2/apps', headers=self.headers, verify=False).json()
        if not response['apps']:
            print("No Apps found on Marathon")
            sys.exit(1)
        else:
            apps = []
            for i in response['apps']:
                appid = i['id'].strip('/')
                apps.append(appid)
            print("Found the following App LIST on Marathon =", apps)
            return apps


def marathon_auth_login(marathon_address, userid, password):
    '''
    Will login to the DCOS ACS Service and RETURN A JWT TOKEN for subsequent API requests to Marathon, Mesos, etc
    '''
    rawdata = {'uid' : userid, 'password' : password}
    login_headers={'Content-type': 'application/json'}
    response = requests.post(marathon_address, headers=login_headers, data=json.dumps(rawdata),verify=False).json()
    auth_token=response['token']
    return auth_token

if __name__ == "__main__":
    import argparse

    print("This application tested with Python3 only")
    parser = argparse.ArgumentParser(description='Marathon autoscale app.')
    parser.add_argument('--marathon_address', help='The DNS hostname or IP of your Marathon Instance', required=True)
    parser.add_argument('--max_mem_percent',
                        help='The Max percent of Mem Usage averaged across all Application Instances to trigger Autoscale (ie. 80)',
                        required=True, type=float)
    parser.add_argument('--max_cpu_time',
                        help='The Max percent of CPU Usage averaged across all Application Instances to trigger Autoscale (ie. 80)',
                        required=True, type=float)
    parser.add_argument('--trigger_mode', help='Which metric(s) to trigger Autoscale (' and ', ' or ')', required=True)
    parser.add_argument('--autoscale_multiplier', help='Autoscale multiplier for triggered Autoscale (ie 1.5)',
                        required=True, type=float)
    parser.add_argument('--max_instances',
                        help='The Max instances that should ever exist for this application (ie. 20)', required=True,
                        type=int)
    parser.add_argument('--userid', help='Username for the DCOS cluster')
    parser.add_argument('--password', help='Password for the DCOS cluster')
    parser.add_argument('--marathon-app',
                        help='Marathon Application Name to Configure Autoscale for from the Marathon UI', required=True)
    parser.add_argument('--min_instances', help='Minimum number of instances to maintain', required=True, type=int)
    parser.add_argument('--cool-down-factor', help='Number of cycles to avoid scaling again', required=True, type=int)
    parser.add_argument('--trigger_number', help='Number of cycles to avoid scaling again', required=True, type=int)
    try:
        args = parser.parse_args()
    except Exception as e:
        parser.print_help()
        sys.exit(1)

    marathon_address = args.marathon_address
    max_mem_percent = float(args.max_mem_percent)
    max_cpu_time = float(args.max_cpu_time)
    trigger_mode = args.trigger_mode
    autoscale_multiplier = float(args.autoscale_multiplier)
    max_instances = float(args.max_instances)
    userid = args.userid
    password = args.password
    marathon_app = args.marathon_app
    min_instances = float(args.min_instances)
    cool_down_factor = float(args.cool_down_factor)
    trigger_number = float(args.trigger_number)

    if userid is not None:
        marathon_auth_token=marathon_auth_login(marathon_address, userid, password)
        print('Auth Token is = ' + marathon_auth_token)
    else:
        marathon_auth_token=None
    running = 1
    # Initialize variables
    cool_down = 0
    trigger_var = 0