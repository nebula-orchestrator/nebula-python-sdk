import os
from unittest import TestCase
from NebulaPythonSDK import Nebula


# the following unit tests require a working nebula manager to test against and having the envvars in the
# nebula_connection function declared if not using the default values
def nebula_connection():
    nebula_user = os.getenv("USER")
    nebula_password = os.getenv("PASSWORD")
    nebula_hostname = os.getenv("HOST", "127.0.0.1")
    nebula_port = int(os.getenv("PORT", "80"))
    nebula_protocol = os.getenv("PROTOCOL", "http")
    nebula_request_timeout = int(os.getenv("REQUEST_TIMEOUT", "60"))
    connection = Nebula(username=nebula_user, password=nebula_password, host=nebula_hostname, port=nebula_port,
                        protocol=nebula_protocol, request_timeout=nebula_request_timeout)
    return connection


class BaseTests(TestCase):

    def test_check_api(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.check_api()
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(reply["reply"]["api_available"], True)

    def test_create_app_success(self):
        # TODO - finish the tests
        pass

    def test_create_app_already_exists(self):
        # TODO - finish the tests
        pass

    def test_create_app_missing_params(self):
        # TODO - finish the tests
        pass

    def test_delete_app_success(self):
        # TODO - finish the tests
        pass

    def test_delete_app_does_not_exist(self, app="test_app_which_does_not_exist"):
        nebula_connection_object = nebula_connection()
        # deleting twice so even if the app does exist prior to running the check it won't on the 2nd run
        nebula_connection_object.delete_app(app)
        reply = nebula_connection_object.delete_app(app)
        self.assertEqual(reply["status_code"], 403)
        self.assertEqual(reply["reply"]["app_exists"], False)

    def test_list_apps(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_apps()
        app_list = reply["reply"]["apps"]
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(isinstance(app_list, list), True)
        for app in app_list:
            self.assertEqual(isinstance(app, unicode), True)

    def test_list_app_info(self, app="test"):
        # TODO - create app before testing it & change the app default name to something that not likely to be used
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_app_info(app)
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(isinstance(reply["reply"]["app_id"], int), True)
        self.assertEqual(isinstance(reply["reply"]["containers_per"], dict), True)
        self.assertEqual(reply["reply"]["app_name"], app)
        self.assertEqual(isinstance(reply["reply"]["devices"], list), True)
        self.assertEqual(isinstance(reply["reply"]["docker_image"], unicode), True)
        self.assertEqual(isinstance(reply["reply"]["env_vars"], dict), True)
        self.assertEqual(isinstance(reply["reply"]["networks"], list), True)
        self.assertEqual(isinstance(reply["reply"]["privileged"], bool), True)
        self.assertEqual(isinstance(reply["reply"]["rolling_restart"], bool), True)
        self.assertEqual(isinstance(reply["reply"]["running"], bool), True)
        self.assertEqual(isinstance(reply["reply"]["starting_ports"], list), True)
        self.assertEqual(isinstance(reply["reply"]["volumes"], list), True)

    def test_stop_app(self):
        # TODO - finish the tests
        pass

    def test_start_app(self):
        # TODO - finish the tests
        pass

    def test_restart_app(self):
        # TODO - finish the tests
        pass

    def test_update_app(self):
        # TODO - finish the tests
        pass

    def test_prune_images(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.prune_images()
        self.assertEqual(reply["status_code"], 202)
        self.assertEqual(isinstance(reply["reply"]["prune_ids"], dict), True)

    def test_prune_device_group_images(self, device_group="test"):
        # TODO - create device_group before testing & change device_group name to something that not likely to be used
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.prune__device_group_images(device_group)
        first_prune_id = reply["reply"]["prune_id"]
        reply = nebula_connection_object.prune__device_group_images(device_group)
        self.assertEqual(reply["status_code"], 202)
        self.assertEqual(reply["reply"]["prune_id"], first_prune_id + 1)

    def test_list_device_group_info(self, device_group="test"):
        # TODO - create app before testing it & change the app default name to something that not likely to be used
        # TODO - create device_group before testing & change device_group name to something that not likely to be used
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_device_group_info(device_group)
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(isinstance(reply["reply"]["prune_id"], int), True)
        self.assertEqual(isinstance(reply["reply"]["device_group_id"], int), True)
        for app in reply["reply"]["apps"]:
            self.assertEqual(isinstance(app["app_id"], int), True)
            self.assertEqual(isinstance(app["containers_per"], dict), True)
            self.assertEqual(isinstance(app["app_name"], unicode), True)
            self.assertEqual(isinstance(app["devices"], list), True)
            self.assertEqual(isinstance(app["docker_image"], unicode), True)
            self.assertEqual(isinstance(app["env_vars"], dict), True)
            self.assertEqual(isinstance(app["networks"], list), True)
            self.assertEqual(isinstance(app["privileged"], bool), True)
            self.assertEqual(isinstance(app["rolling_restart"], bool), True)
            self.assertEqual(isinstance(app["running"], bool), True)
            self.assertEqual(isinstance(app["starting_ports"], list), True)
            self.assertEqual(isinstance(app["volumes"], list), True)

    def test_list_device_group(self, device_group="test"):
        # TODO - create device_group before testing & change device_group name to something that not likely to be used
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_device_group(device_group)
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(isinstance(reply["reply"]["device_group_id"], int), True)
        self.assertEqual(isinstance(reply["reply"]["apps"], list), True)
        self.assertEqual(reply["reply"]["device_group"], device_group)

    def test_list_device_groups(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_device_groups()
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(isinstance(reply["reply"]["device_groups"], list), True)

    def test_create_device_group_success(self):
        # TODO - finish the tests
        pass

    def test_create_device_group_already_exists(self):
        # TODO - finish the tests
        pass

    def test_delete_device_group_success(self):
        # TODO - finish the tests
        pass

    def test_delete_device_group_does_not_exists(self, device_group="test_non_existing_group"):
        nebula_connection_object = nebula_connection()
        # deleting twice so even if the device_group doesn't exist prior to running the check prior to running the
        # check it won't on the 2nd run
        nebula_connection_object.delete_device_group(device_group)
        reply = nebula_connection_object.delete_device_group(device_group)
        self.assertEqual(reply["status_code"], 403)
        self.assertEqual(reply["reply"]["device_group_exists"], False)

    def test_update_device_group(self):
        # TODO - finish the tests
        pass
