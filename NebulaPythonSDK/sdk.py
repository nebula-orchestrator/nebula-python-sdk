import requests, base64, json


class Nebula:

    def __init__(self, username, password, host, protocol="http"):
        self.username = username
        self.password = password
        self.protocol = protocol
        self.host = protocol + "://" + host
        self.basic_auth = base64.b64encode(username + ":" + password)
        self.headers = {
            'authorization': "Basic " + self.basic_auth,
            'content-type': "application/json",
            'cache-control': "no-cache"
        }

    def create_app(self, app, config):
        url = self.host + "/api/apps/" + app
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers)
        return response

    def delete_app(self, app):
        url = self.host + "/api/apps/" + app
        headers = self.headers
        response = requests.request("DELETE", url, headers=headers)
        return response

    def list_apps(self):
        url = self.host + "/api/apps"
        headers = self.headers
        response = requests.request("GET", url, headers=headers)
        return response

    def list_app_info(self, app):
        url = self.host + "/api/apps/" + app
        headers = self.headers
        response = requests.request("GET", url, headers=headers)
        return response

    def stop_app(self, app):
        url = self.host + "/api/apps/" + app + "/stop"
        headers = self.headers
        response = requests.request("POST", url, headers=headers)
        return response

    def start_app(self, app):
        url = self.host + "/api/apps/" + app + "/start"
        headers = self.headers
        response = requests.request("POST", url, headers=headers)
        return response

    def restart_app(self, app):
        url = self.host + "/api/apps/" + app + "/restart"
        headers = self.headers
        response = requests.request("POST", url, headers=headers)
        return response

    def update_app(self, app, config):
        url = self.host + "/api/apps/" + app + "/update"
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers)
        return response

    def roll_app(self, app):
        url = self.host + "/api/apps/" + app + "/roll"
        headers = self.headers
        response = requests.request("POST", url, headers=headers)
        return response
