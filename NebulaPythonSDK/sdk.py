import requests, base64, json, six


def b64encode(source):
    if six.PY3:
        source = source.encode('utf-8')
    content = base64.b64encode(source).decode('utf-8')


class Nebula:

    # the nebula class init module serves as the login against the nebula API as it's the only shared thing among the
    # class functions
    def __init__(self, username=None, password=None, token=None, host="127.0.0.1", port=80, protocol="http",
                 request_timeout=60):
        self.request_timeout = request_timeout
        self.username = username
        self.password = password
        self.token = token
        self.protocol = protocol
        self.port = port
        self.host = protocol + "://" + host + ":" + str(port)
        self.headers = {
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        if token is not None:
            self.headers["authorization"] = "Bearer " + self.token
        elif username is not None and password is not None:
            user_pass_combo = username + ":" + password
            if six.PY3 is True:
                user_pass_combo = user_pass_combo.encode('utf-8')
            self.basic_auth = base64.b64encode(user_pass_combo)
            self.headers["authorization"] = "Basic " + self.basic_auth.decode('utf-8')
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

    # create a new nebula device_group, requires the app name to create and a complete dict of the config values for it
    def create_device_group(self, device_group, config):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups/" + device_group
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # delete an existing nebula device_group, no confirmation required in SDK so be careful
    def delete_device_group(self, device_group):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups/" + device_group
        headers = self.headers
        response = requests.request("DELETE", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # update a device group
    def update_device_group(self, device_group, config):
        url = self.host + "/api/" + self.API_VERSION + "/device_groups/" + device_group + "/update"
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("PUT", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list device_group configuration
    def list_reports(self, page_size=10, hostname=None, device_group=None, report_creation_time_filter="gt",
                     report_creation_time=None, last_id=None):
        url = self.host + "/api/" + self.API_VERSION + "/reports"
        headers = self.headers
        querystring = {
            "page_size": page_size,
            "hostname": hostname,
            "device_group": device_group,
            "report_creation_time_filter": report_creation_time_filter,
            "report_creation_time": report_creation_time,
            "last_id": last_id
        }
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout, params=querystring)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list all users
    def list_users(self):
        url = self.host + "/api/" + self.API_VERSION + "/users"
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list a user configuration
    def list_user(self, user):
        url = self.host + "/api/" + self.API_VERSION + "/users/" + user
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # delete an existing nebula user, no confirmation required in SDK so be careful
    def delete_user(self, user):
        url = self.host + "/api/" + self.API_VERSION + "/users/" + user
        headers = self.headers
        response = requests.request("DELETE", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # update a user pass and\or bearer token
    def update_user(self, user, config):
        url = self.host + "/api/" + self.API_VERSION + "/users/" + user + "/update"
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("PUT", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # refresh a token for a user
    def refresh_user_token(self, user):
        url = self.host + "/api/" + self.API_VERSION + "/users/" + user + "/refresh"
        headers = self.headers
        response = requests.request("POST", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # create a new nebula user, requires the user name to create and a complete dict of the config values for it
    def create_user(self, user, config):
        url = self.host + "/api/" + self.API_VERSION + "/users/" + user
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list all user groups
    def list_user_groups(self):
        url = self.host + "/api/" + self.API_VERSION + "/user_groups"
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list a user group configuration
    def list_user_group(self, user):
        url = self.host + "/api/" + self.API_VERSION + "/user_groups/" + user
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # delete an existing nebula user group, no confirmation required in SDK so be careful
    def delete_user_group(self, user):
        url = self.host + "/api/" + self.API_VERSION + "/user_groups/" + user
        headers = self.headers
        response = requests.request("DELETE", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # update a user group
    def update_user_group(self, user, config):
        url = self.host + "/api/" + self.API_VERSION + "/user_groups/" + user + "/update"
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("PUT", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # create a new nebula user group, requires the group name to create and a complete dict of the config values for it
    def create_user_group(self, user, config):
        url = self.host + "/api/" + self.API_VERSION + "/user_groups/" + user
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list all of the cron_jobs managed by nebula
    def list_cron_jobs(self):
        url = self.host + "/api/" + self.API_VERSION + "/cron_jobs"
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # delete an existing nebula cron_job, no confirmation required in SDK so be careful
    def delete_cron_job(self, cron_job):
        url = self.host + "/api/" + self.API_VERSION + "/cron_jobs/" + cron_job
        headers = self.headers
        response = requests.request("DELETE", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # list the config of a nebula cron_job, only requires the app name
    def list_cron_job_info(self, cron_job):
        url = self.host + "/api/" + self.API_VERSION + "/cron_jobs/" + cron_job
        headers = self.headers
        response = requests.request("GET", url, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # create a new nebula cron_job, requires the cron_job name to create and a complete dict of the config values for it
    def create_cron_job(self, cron_job, config):
        url = self.host + "/api/" + self.API_VERSION + "/cron_jobs/" + cron_job
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("POST", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response

    # update a nebula cron_job, requires the cron_job name and a dict of the config values you want to change, any
    # combination of config values is accepted as it keeps the rest unchanged
    def update_cron_job(self, cron_job, config):
        url = self.host + "/api/" + self.API_VERSION + "/cron_jobs/" + cron_job + "/update"
        payload = json.dumps(config)
        headers = self.headers
        response = requests.request("PUT", url, data=payload, headers=headers, timeout=self.request_timeout)
        filtered_response = {"status_code": response.status_code, "reply": response.json()}
        return filtered_response
