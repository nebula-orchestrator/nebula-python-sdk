from unittest import TestCase
import os
from NebulaPythonSDK.sdk import Nebula


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

    def test_delete_app_does_not_exist(self):
        # TODO - finish the tests
        pass

    def test_list_apps(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_apps()
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(isinstance(reply["reply"]["apps"], list), True)

    def test_list_app_info(self, app="test"):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_app_info(app)
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(reply["reply"]["app_name"], app)

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
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.prune__device_group_images(device_group)
        first_prune_id = reply["reply"]["prune_id"]
        reply = nebula_connection_object.prune__device_group_images(device_group)
        self.assertEqual(reply["status_code"], 202)
        self.assertEqual(reply["reply"]["prune_id"], first_prune_id + 1)

    def test_list_device_group_info(self, device_group="test"):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_device_group_info(device_group)
        self.assertEqual(reply["status_code"], 200)

    def test_list_device_group(self, device_group="test"):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_device_group(device_group)
        self.assertEqual(reply["status_code"], 200)

    def test_list_device_groups(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_device_groups()
        self.assertEqual(reply["status_code"], 200)

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
        reply = nebula_connection_object.delete_device_group(device_group)
        self.assertEqual(reply["status_code"], 403)

    def test_update_device_group(self):
        # TODO - finish the tests
        pass
