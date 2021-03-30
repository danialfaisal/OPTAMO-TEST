import requests
import json
from requests.auth import HTTPBasicAuth
import os

path = '/Users/danialfaisal/Desktop/OPTAMO-Project/data-optamo/'
username = 'optamo'
password = 'optamo1234'

files = [i for i in os.listdir(path)if os.path.isfile(os.path.join(path,i))]

# for production environment use below url
url = 'https://optamo-backend.herokuapp.com/api/weather/'

# for local environment use below url
# url = "http://127.0.0.1:8000/api/weather/"


for i in files:
    if 'state06' in i:
        fname = path + i
        with open(fname, 'r') as f:
            lines = f.read().splitlines()
            tmin_line = lines[-1]
            tmin = tmin_line.split()
            tmax_line = lines[-2]
            tmax = tmax_line.split()
            snow_line = lines[-3]
            snow = snow_line.split()
            prcp_line = lines[-5]
            prcp = prcp_line.split()

            state = "Connecticut"
            station_id = tmin[0]
            tmin_data = tmin[5]
            tmax_data = tmax[5]
            snow_data = snow[5]
            prcp_data = prcp[4]

            data = {
                'station_id': station_id,
                'state': state,
                'precipitation': prcp_data,
                'temp_min': tmin_data,
                'temp_max': tmax_data,
                'snowfall': snow_data,
            }
            body = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

            # Making http post request
            response = requests.post(url, headers=headers, data=body, verify=False,
                                     auth=HTTPBasicAuth(username, password))
            print(body)
            print(response.json())



    elif 'state17' in i:
        fname = path + i
        with open(fname, 'r') as f:
            lines = f.read().splitlines()
            tmin_line = lines[-1]
            tmin = tmin_line.split()
            tmax_line = lines[-2]
            tmax = tmax_line.split()
            snow_line = lines[-3]
            snow = snow_line.split()
            prcp_line = lines[-5]
            prcp = prcp_line.split()

            state = "Maine"
            station_id = tmin[0]
            tmin_data = tmin[5]
            tmax_data = tmax[5]
            snow_data = snow[5]
            prcp_data = prcp[4]

            data = {
                'station_id': station_id,
                'state': state,
                'precipitation': prcp_data,
                'temp_min': tmin_data,
                'temp_max': tmax_data,
                'snowfall': snow_data,
            }
            body = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

            # Making http post request
            response = requests.post(url, headers=headers, data=body, verify=False,
                                     auth=HTTPBasicAuth(username, password))
            print(body)
            print(response.json())


    elif 'state19' in i:
        fname = path + i
        with open(fname, 'r') as f:
            lines = f.read().splitlines()
            tmin_line = lines[-1]
            tmin = tmin_line.split()
            tmax_line = lines[-2]
            tmax = tmax_line.split()
            snow_line = lines[-3]
            snow = snow_line.split()
            prcp_line = lines[-5]
            prcp = prcp_line.split()

            state = "Massachusetts"
            station_id = tmin[0]
            tmin_data = tmin[5]
            tmax_data = tmax[5]
            snow_data = snow[5]
            prcp_data = prcp[4]

            data = {
                'station_id': station_id,
                'state': state,
                'precipitation': prcp_data,
                'temp_min': tmin_data,
                'temp_max': tmax_data,
                'snowfall': snow_data,
            }
            body = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

            # Making http post request
            response = requests.post(url, headers=headers, data=body, verify=False,
                                     auth=HTTPBasicAuth(username, password))
            print(body)
            print(response.json())

    elif 'state27' in i:
        fname = path + i
        with open(fname, 'r') as f:
            lines = f.read().splitlines()
            tmin_line = lines[-1]
            tmin = tmin_line.split()
            tmax_line = lines[-2]
            tmax = tmax_line.split()
            snow_line = lines[-3]
            snow = snow_line.split()
            prcp_line = lines[-5]
            prcp = prcp_line.split()

            state = "New Hampshire"
            station_id = tmin[0]
            tmin_data = tmin[5]
            tmax_data = tmax[5]
            snow_data = snow[5]
            prcp_data = prcp[4]

            data = {
                'station_id': station_id,
                'state': state,
                'precipitation': prcp_data,
                'temp_min': tmin_data,
                'temp_max': tmax_data,
                'snowfall': snow_data,
            }
            body = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

            # Making http post request
            response = requests.post(url, headers=headers, data=body, verify=False,
                                     auth=HTTPBasicAuth(username, password))
            print(body)
            print(response.json())


    elif 'state28' in i:
        fname = path + i
        with open(fname, 'r') as f:
            lines = f.read().splitlines()
            tmin_line = lines[-1]
            tmin = tmin_line.split()
            tmax_line = lines[-2]
            tmax = tmax_line.split()
            snow_line = lines[-3]
            snow = snow_line.split()
            prcp_line = lines[-5]
            prcp = prcp_line.split()

            state = "New Jersey"
            station_id = tmin[0]
            tmin_data = tmin[5]
            tmax_data = tmax[5]
            snow_data = snow[5]
            prcp_data = prcp[4]

            data = {
                'station_id': station_id,
                'state': state,
                'precipitation': prcp_data,
                'temp_min': tmin_data,
                'temp_max': tmax_data,
                'snowfall': snow_data,
            }
            body = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

            # Making http post request
            response = requests.post(url, headers=headers, data=body, verify=False,
                                     auth=HTTPBasicAuth(username, password))
            print(body)
            print(response.json())


    elif 'state30' in i:
        fname = path + i
        with open(fname, 'r') as f:
            lines = f.read().splitlines()
            tmin_line = lines[-1]
            tmin = tmin_line.split()
            tmax_line = lines[-2]
            tmax = tmax_line.split()
            snow_line = lines[-3]
            snow = snow_line.split()
            prcp_line = lines[-5]
            prcp = prcp_line.split()

            state = "New York"
            station_id = tmin[0]
            tmin_data = tmin[5]
            tmax_data = tmax[5]
            snow_data = snow[5]
            prcp_data = prcp[4]

            data = {
                'station_id': station_id,
                'state': state,
                'precipitation': prcp_data,
                'temp_min': tmin_data,
                'temp_max': tmax_data,
                'snowfall': snow_data,
            }
            body = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

            # Making http post request
            response = requests.post(url, headers=headers, data=body, verify=False,
                                     auth=HTTPBasicAuth(username, password))
            print(body)
            print(response.json())


    elif 'state36' in i:
        fname = path + i
        with open(fname, 'r') as f:
            lines = f.read().splitlines()
            tmin_line = lines[-1]
            tmin = tmin_line.split()
            tmax_line = lines[-2]
            tmax = tmax_line.split()
            snow_line = lines[-3]
            snow = snow_line.split()
            prcp_line = lines[-5]
            prcp = prcp_line.split()

            state = "Pennsylvania"
            station_id = tmin[0]
            tmin_data = tmin[5]
            tmax_data = tmax[5]
            snow_data = snow[5]
            prcp_data = prcp[4]

            data = {
                'station_id': station_id,
                'state': state,
                'precipitation': prcp_data,
                'temp_min': tmin_data,
                'temp_max': tmax_data,
                'snowfall': snow_data,
            }
            body = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

            # Making http post request
            response = requests.post(url, headers=headers, data=body, verify=False,
                                     auth=HTTPBasicAuth(username, password))
            print(body)
            print(response.json())


    elif 'state37' in i:
        fname = path + i
        with open(fname, 'r') as f:
            lines = f.read().splitlines()
            tmin_line = lines[-1]
            tmin = tmin_line.split()
            tmax_line = lines[-2]
            tmax = tmax_line.split()
            snow_line = lines[-3]
            snow = snow_line.split()
            prcp_line = lines[-5]
            prcp = prcp_line.split()

            state = "Rhode Island"
            station_id = tmin[0]
            tmin_data = tmin[5]
            tmax_data = tmax[5]
            snow_data = snow[5]
            prcp_data = prcp[4]

            data = {
                'station_id': station_id,
                'state': state,
                'precipitation': prcp_data,
                'temp_min': tmin_data,
                'temp_max': tmax_data,
                'snowfall': snow_data,
            }
            body = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

            # Making http post request
            response = requests.post(url, headers=headers, data=body, verify=False,
                                     auth=HTTPBasicAuth(username, password))
            print(body)
            print(response.json())

    elif 'state43' in i:
        fname = path + i
        with open(fname, 'r') as f:
            lines = f.read().splitlines()
            tmin_line = lines[-1]
            tmin = tmin_line.split()
            tmax_line = lines[-2]
            tmax = tmax_line.split()
            snow_line = lines[-3]
            snow = snow_line.split()
            prcp_line = lines[-5]
            prcp = prcp_line.split()

            state = "Vermont"
            station_id = tmin[0]
            tmin_data = tmin[5]
            tmax_data = tmax[5]
            snow_data = snow[5]
            prcp_data = prcp[4]

            data = {
                'station_id': station_id,
                'state': state,
                'precipitation': prcp_data,
                'temp_min': tmin_data,
                'temp_max': tmax_data,
                'snowfall': snow_data,
            }
            body = json.dumps(data)
            headers = {'Content-Type': 'application/json'}

            # Making http post request
            response = requests.post(url, headers=headers, data=body, verify=False,
                                     auth=HTTPBasicAuth(username, password))
            print(body)
            print(response.json())