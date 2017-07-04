import requests, base64, json


class Nebula:

    # the nebula class init module serves as the login against the nebula API as it's the only shared thing among the
    # class functions
    def __init__(self, username, password, host, port=80, protocol="http"):
        self.username = username
        self.password = password
        self.protocol = protocol
        self.protocol = port
        self.host = protocol + "://" + host + ":" + str(port)
        self.basic_auth = base64.b64encode(username + ":" + password)
        self.headers = {
            'authorization': "Basic " + self.basic_auth,
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

    # create a new nebula app, requires the app name to create and a complete dict of the config values for it
    def create_app(self, app, config):
        url = self.host + "/api/apps/" + app
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers)
        return response

    # delete an existing nebula app, no confirmation required in SDK so be careful
    def delete_app(self, app):
        url = self.host + "/api/apps/" + app
        headers = self.headers
        response = requests.request("DELETE", url, headers=headers)
        return response

    # list all of the apps managed by nebula
    def list_apps(self):
        url = self.host + "/api/apps"
        headers = self.headers
        response = requests.request("GET", url, headers=headers)
        return response

    # list the config of a nebula app, only requires the app name
    def list_app_info(self, app):
        url = self.host + "/api/apps/" + app
        headers = self.headers
        response = requests.request("GET", url, headers=headers)
        return response

    # stop a nebula app, only requires the app name
    def stop_app(self, app):
        url = self.host + "/api/apps/" + app + "/stop"
        headers = self.headers
        response = requests.request("POST", url, headers=headers)
        return response

    # start a nebula app, only requires the app name
    def start_app(self, app):
        url = self.host + "/api/apps/" + app + "/start"
        headers = self.headers
        response = requests.request("POST", url, headers=headers)
        return response

    # restart a nebula app, only requires the app name
    def restart_app(self, app):
        url = self.host + "/api/apps/" + app + "/restart"
        headers = self.headers
        response = requests.request("POST", url, headers=headers)
        return response

    # update a nebula app, requires the app name and a dict of the config values you want to change, any combination of
    # config values is accepted as it keeps the rest unchanged
    def update_app(self, app, config):
        url = self.host + "/api/apps/" + app + "/update"
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("PUT", url, data=payload, headers=headers)
        return response

    # rolling restart an app, only requires the app name
    def roll_app(self, app):
        url = self.host + "/api/apps/" + app + "/roll"
        headers = self.headers
        response = requests.request("POST", url, headers=headers)
        return response

    # check that the contacted api is responding as expected
    def check_api(self):
        url = self.host + "/api/status"
        headers = self.headers
        response = requests.request("GET", url, headers=headers)
        return response
