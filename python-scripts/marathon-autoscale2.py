import sys
import requests
import json
# import math
import time
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
    def __init__(self, marathon_address):
        self.name = marathon_address
        self.uri = marathon_address
        self.headers = {'Content-type': 'application/json'}
        self.apps = self.get_all_apps()

    def get_all_apps(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(self.uri + '/v2/apps', headers=self.headers, verify=False, auth=(userid, password)).json()
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

    def get_app_details(self, marathon_app):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.get(self.uri + '/v2/apps/'+ marathon_app, headers=self.headers, verify=False, auth=(userid, password)).json()
        if (response['app']['tasks'] ==[]):
            print ('No task data on Marathon for App !', marathon_app)
        else:
            app_instances = response['app']['instances']
            self.appinstances = app_instances
            print(marathon_app, "has", self.appinstances, "deployed instances")
            app_task_dict={}
            for i in response['app']['tasks']:
                taskid = i['id']
                hostid = i['host']
                slaveId=i['slaveId']
                print ('DEBUG - taskId=', taskid +' running on '+hostid + 'which is Mesos Slave Id '+slaveId)
                app_task_dict[str(taskid)] = str(slaveId)
            return app_task_dict

    # def scale_app(self,marathon_app, autoscale_multiplier):
    #     target_instances_float=self.appinstances * autoscale_multiplier
    #     target_instances=math.ceil(target_instances_float)
    #     if (target_instances > max_instances):
    #         print("Reached the set maximum instances of", max_instances)
    #         target_instances=max_instances
    #     else:
    #         target_instances=target_instances
    #     data ={'instances': target_instances}
    #     json_data=json.dumps(data)
    #     #headers = {'Content-type': 'application/json'}
    #     response=requests.put(self.uri + '/v2/apps/'+ marathon_app, json_data,headers=self.headers,verify=False, auth=(userid, password))
    #     print ('Scale_app return status code =', response.status_code)
    #
    # def scale_down_app(self, marathon_app, autoscale_multiplier):
    #     target_instances=math.ceil(self.appinstances / autoscale_multiplier)
    #     if (target_instances < min_instances):
    #         print("No scale, reached the minimum instances of ", min_instances)
    #         target_instances=min_instances
    #     else:
    #         target_instances=target_instances
    #     if (self.appinstances != target_instances):
    #         data ={'instances': target_instances}
    #         json_data=json.dumps(data)
    #         #headers = {'Content-type': 'application/json'}
    #         response=requests.put(self.uri + '/v2/apps/'+ marathon_app, json_data, headers=self.headers,verify=False)
    #         print ('Scale_down_app return status code =', response.status_code)

def timer():
    print("Successfully completed a cycle, sleeping for 30 seconds ...")
    time.sleep(30)
    return

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

    running = 1
    # Initialize variables
    cool_down = 0
    trigger_var = 0
    while running == 1:
        # Initialize the Marathon object
        aws_marathon = Marathon(marathon_address)
        print("Marathon URI = ...", aws_marathon.uri)
        print("Marathon Headers = ...", aws_marathon.headers)
        print("Marathon name = ...", aws_marathon.name)
        # Call get_all_apps method for new object created from aws_marathon class and return all apps
        marathon_apps = aws_marathon.get_all_apps()
        print ("The following apps exist in Marathon...", marathon_apps)
        # Quick sanity check to test for apps existence in MArathon.
        if (marathon_app in marathon_apps):
            print ("  Found your Marathon App=", marathon_app)
        else:
            print ("  Could not find your App =", marathon_app)
            timer()
            continue
        # Return a dictionary comprised of the target app taskId and hostId.
        app_task_dict = aws_marathon.get_app_details(marathon_app)
        print ("    Marathon  App 'tasks' for", marathon_app, "are=", app_task_dict)