import requests, base64, json


class Nebula:

    # the nebula class init module serves as the login against the nebula API as it's the only shared thing among the
    # class functions
    def __init__(self, username=None, password=None, host="127.0.0.1", port=80, protocol="http", request_timeout=60):
        self.request_timeout = request_timeout
        self.username = username
        self.password = password
        self.protocol = protocol
        self.port = port
        self.host = protocol + "://" + host + ":" + str(port)
        self.headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        if username is not None and password is not None:
            self.basic_auth = base64.b64encode(username + ":" + password)
            self.headers["authorization"] = "Basic " + self.basic_auth
        self.API_VERSION = "v2"

    # create a new nebula app, requires the app name to create and a complete dict of the config values for it
    def create_app(self, app, config):
        url = self.host + "/api/" + self.API_VERSION + "/apps/" + app
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # delete an existing nebula app, no confirmation required in SDK so be careful
    def delete_app(self, app):
        url = self.host + "/api/" + self.API_VERSION + "/apps/" + app
        headers = self.headers
        response = requests.request("DELETE", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list all of the apps managed by nebula
    def list_apps(self):
        url = self.host + "/api/" + self.API_VERSION + "/apps"
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list the config of a nebula app, only requires the app name
    def list_app_info(self, app):
        url = self.host + "/api/" + self.API_VERSION + "/apps/" + app
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # stop a nebula app, only requires the app name
    def stop_app(self, app):
        url = self.host + "/api/" + self.API_VERSION + "/apps/" + app + "/stop"
        headers = self.headers
        response = requests.request("POST", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # start a nebula app, only requires the app name
    def start_app(self, app):
        url = self.host + "/api/" + self.API_VERSION + "/apps/" + app + "/start"
        headers = self.headers
        response = requests.request("POST", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # restart a nebula app, only requires the app name
    def restart_app(self, app):
        url = self.host + "/api/" + self.API_VERSION + "/apps/" + app + "/restart"
        headers = self.headers
        response = requests.request("POST", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # update a nebula app, requires the app name and a dict of the config values you want to change, any combination of
    # config values is accepted as it keeps the rest unchanged
    def update_app(self, app, config):
        url = self.host + "/api/" + self.API_VERSION + "/apps/" + app + "/update"
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("PUT", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # prune unused images on all devices
    def prune_images(self):
        url = self.host + "/api/" + self.API_VERSION + "/prune"
        headers = self.headers
        response = requests.request("POST", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # prune unused images on all devices that are part of the device_group given
    def prune__device_group_images(self, device_groups):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups/" + device_groups + "/prune"
        headers = self.headers
        response = requests.request("POST", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # check that the contacted api is responding as expected
    def check_api(self):
        url = self.host + "/api/" + self.API_VERSION + "/status"
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list the info of all apps and all data of a given device_group
    def list_device_group_info(self, device_group):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups/" + device_group + "/info"
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list all device_groups
    def list_device_groups(self):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups"
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list device_group configuration
    def list_device_group(self, device_group):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups/" + device_group
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # create a new nebula delete_device_group, requires the app name to create and a complete dict of the config values
    # for it
    def create_device_group(self, device_group, config):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups/" + device_group
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # delete an existing nebula delete_device_group, no confirmation required in SDK so be careful
    def delete_device_group(self, device_group):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups/" + device_group
        headers = self.headers
        response = requests.request("DELETE", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # update apps in a device group
    def update_device_group(self, device_group, config):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups/" + device_group + "/update"
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response
