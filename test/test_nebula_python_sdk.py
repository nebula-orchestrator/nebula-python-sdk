import os
from unittest import TestCase
from NebulaPythonSDK import Nebula


# the following unit tests require a working nebula manager to test against and having the envvars in the
# nebula_connection function declared if not using the default values
def nebula_connection():
    nebula_user = os.getenv("NEBULA_TEST_USERNAME", "nebula")
    nebula_password = os.getenv("NEBULA_TEST_PASSWORD", "nebula")
    nebula_hostname = os.getenv("NEBULA_TEST_HOST", "127.0.0.1")
    nebula_port = int(os.getenv("NEBULA_TEST_PORT", "80"))
    nebula_protocol = os.getenv("NEBULA_TEST_PROTOCOL", "http")
    nebula_request_timeout = int(os.getenv("NEBULA_TEST_REQUEST_TIMEOUT", "60"))
    connection = Nebula(username=nebula_user, password=nebula_password, host=nebula_hostname, port=nebula_port,
                        protocol=nebula_protocol, request_timeout=nebula_request_timeout)
    return connection


def create_temp_app(nebula_connection_object, app):
    app_conf = {
        "starting_ports": [80],
        "containers_per": {"server": 1},
        "env_vars": {"TEST": "test123"},
        "docker_image": "nginx",
        "running": True,
        "volumes": [],
        "networks": ["nebula", "bridge"],
        "devices": [],
        "privileged": False,
        "rolling_restart": False
    }
    reply = nebula_connection_object.create_app(app, app_conf)
    return reply


class BaseTests(TestCase):

    def test_check_api(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.check_api()
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(reply["reply"]["api_available"], True)

    def test_app_flow(self, app="unit_test_app"):
        nebula_connection_object = nebula_connection()

        # make sure app does not exist before the unit test runs
        nebula_connection_object.delete_app(app)

        # check app creation works
        reply = create_temp_app(nebula_connection_object, app)
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(reply["reply"]["app_id"], 1)
        self.assertEqual(reply["reply"]["containers_per"], {"server": 1})
        self.assertEqual(reply["reply"]["app_name"], app)
        self.assertEqual(reply["reply"]["devices"], [])
        self.assertEqual(reply["reply"]["docker_image"], "nginx")
        self.assertEqual(reply["reply"]["env_vars"], {"TEST": "test123"})
        self.assertEqual(reply["reply"]["networks"], ["nebula", "bridge"])
        self.assertFalse(reply["reply"]["privileged"])
        self.assertFalse(reply["reply"]["rolling_restart"])
        self.assertTrue(reply["reply"]["running"])
        self.assertEqual(reply["reply"]["starting_ports"], [80])
        self.assertEqual(reply["reply"]["volumes"], [])

        # check app info works
        reply = nebula_connection_object.list_app_info(app)
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(reply["reply"]["app_id"], 1)
        self.assertEqual(reply["reply"]["containers_per"], {"server": 1})
        self.assertEqual(reply["reply"]["app_name"], app)
        self.assertEqual(reply["reply"]["devices"], [])
        self.assertEqual(reply["reply"]["docker_image"], "nginx")
        self.assertEqual(reply["reply"]["env_vars"], {"TEST": "test123"})
        self.assertEqual(reply["reply"]["networks"], ["nebula", "bridge"])
        self.assertFalse(reply["reply"]["privileged"])
        self.assertFalse(reply["reply"]["rolling_restart"])
        self.assertTrue(reply["reply"]["running"])
        self.assertEqual(reply["reply"]["starting_ports"], [80])
        self.assertEqual(reply["reply"]["volumes"], [])

        # check that the reply in the case of trying to reuse an existing app name works
        reply = create_temp_app(nebula_connection_object, app)
        self.assertEqual(reply["status_code"], 403)

        # check app stop works
        reply = nebula_connection_object.stop_app(app)
        self.assertEqual(reply["status_code"], 202)
        self.assertFalse(reply["reply"]["running"])
        self.assertEqual(reply["reply"]["app_id"], 2)

        # check app start works
        reply = nebula_connection_object.start_app(app)
        self.assertEqual(reply["status_code"], 202)
        self.assertTrue(reply["reply"]["running"])
        self.assertEqual(reply["reply"]["app_id"], 3)

        # check app restart works
        reply = nebula_connection_object.restart_app(app)
        self.assertEqual(reply["status_code"], 202)
        self.assertEqual(reply["reply"]["app_id"], 4)

        # check app update works
        reply = nebula_connection_object.update_app(app, {"docker_image": "httpd:alpine"})
        self.assertEqual(reply["status_code"], 202)
        self.assertEqual(reply["reply"]["app_id"], 5)
        self.assertEqual(reply["reply"]["docker_image"], "httpd:alpine")

        # check app deletion works
        reply = nebula_connection_object.delete_app(app)
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(reply["reply"], {})

        # check app creation failure with missing params
        reply = nebula_connection_object.create_app(app, {})
        self.assertEqual(reply["status_code"], 400)
        self.assertTrue(isinstance(reply["reply"]["missing_parameters"], list))

    def test_delete_app_does_not_exist(self, app="test_app_which_does_not_exist"):
        nebula_connection_object = nebula_connection()
        # deleting twice so even if the app does exist prior to running the check it won't on the 2nd run
        nebula_connection_object.delete_app(app)
        reply = nebula_connection_object.delete_app(app)
        self.assertEqual(reply["status_code"], 403)
        self.assertFalse(reply["reply"]["app_exists"])

    def test_list_apps(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_apps()
        app_list = reply["reply"]["apps"]
        self.assertEqual(reply["status_code"], 200)
        self.assertTrue(isinstance(app_list, list))
        for app in app_list:
            self.assertTrue(isinstance(app, unicode))

    def test_prune_images(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.prune_images()
        self.assertEqual(reply["status_code"], 202)
        self.assertTrue(isinstance(reply["reply"]["prune_ids"], dict))

    def test_device_group_flow(self, device_group="unit_test_device_group", app="unit_test_device_group_app"):
        nebula_connection_object = nebula_connection()

        # make sure app & device group don't exist before the unit test runs
        nebula_connection_object.delete_app(app)
        nebula_connection_object.delete_device_group(device_group)

        # create app that will be part of the device group
        create_temp_app(nebula_connection_object, app)

        # check device_group creation works
        device_group_config = {"apps": [app]}
        reply = nebula_connection_object.create_device_group(device_group, device_group_config)
        self.assertEqual(reply["status_code"], 200)
        self.assertTrue(reply["reply"]["device_group_id"], 1)
        self.assertTrue(reply["reply"]["apps"], [app])
        self.assertEqual(reply["reply"]["prune_id"], 1)

        # check list device_group works
        reply = nebula_connection_object.list_device_group(device_group)
        self.assertEqual(reply["status_code"], 200)
        self.assertTrue(reply["reply"]["device_group_id"], 1)
        self.assertTrue(reply["reply"]["apps"], [app])
        self.assertEqual(reply["reply"]["prune_id"], 1)

        # check device_group_info works
        reply = nebula_connection_object.list_device_group_info(device_group)
        self.assertEqual(reply["status_code"], 200)
        self.assertTrue(isinstance(reply["reply"]["prune_id"], int))
        self.assertTrue(isinstance(reply["reply"]["device_group_id"], int))
        self.assertTrue(isinstance(reply["reply"]["apps_list"], list))
        for app_reply in reply["reply"]["apps"]:
            self.assertTrue(isinstance(app_reply["app_id"], int))
            self.assertTrue(isinstance(app_reply["containers_per"], dict))
            self.assertTrue(isinstance(app_reply["app_name"], unicode))
            self.assertTrue(isinstance(app_reply["devices"], list))
            self.assertTrue(isinstance(app_reply["docker_image"], unicode))
            self.assertTrue(isinstance(app_reply["env_vars"], dict))
            self.assertTrue(isinstance(app_reply["networks"], list))
            self.assertTrue(isinstance(app_reply["privileged"], bool))
            self.assertTrue(isinstance(app_reply["rolling_restart"], bool))
            self.assertTrue(isinstance(app_reply["running"], bool))
            self.assertTrue(isinstance(app_reply["starting_ports"], list))
            self.assertTrue(isinstance(app_reply["volumes"], list))

        # check prune device_group images works
        reply = nebula_connection_object.prune__device_group_images(device_group)
        first_prune_id = reply["reply"]["prune_id"]
        reply = nebula_connection_object.prune__device_group_images(device_group)
        self.assertEqual(reply["status_code"], 202)
        self.assertEqual(reply["reply"]["prune_id"], first_prune_id + 1)

        # check update device_group works
        reply = nebula_connection_object.update_device_group(device_group, {"apps": []})
        self.assertEqual(reply["status_code"], 202)
        self.assertTrue(reply["reply"]["device_group_id"], 2)
        self.assertTrue(isinstance(reply["reply"]["apps"], list))

        # check device_group already exists works
        device_group_config = {"apps": [app]}
        reply = nebula_connection_object.create_device_group(device_group, device_group_config)
        self.assertEqual(reply["status_code"], 403)

        # check delete device_group works
        reply = nebula_connection_object.delete_device_group(device_group)
        self.assertEqual(reply["status_code"], 200)
        self.assertEqual(reply["reply"], {})

        # clean up app created for the unit test
        nebula_connection_object.delete_app(app)

    def test_list_device_groups(self):
        nebula_connection_object = nebula_connection()
        reply = nebula_connection_object.list_device_groups()
        self.assertEqual(reply["status_code"], 200)
        self.assertTrue(isinstance(reply["reply"]["device_groups"], list))

    def test_delete_device_group_does_not_exists(self, device_group="test_non_existing_group"):
        nebula_connection_object = nebula_connection()
        # deleting twice so even if the device_group doesn't exist prior to running the check prior to running the
        # check it won't on the 2nd run
        nebula_connection_object.delete_device_group(device_group)
        reply = nebula_connection_object.delete_device_group(device_group)
        self.assertEqual(reply["status_code"], 403)
        self.assertFalse(reply["reply"]["device_group_exists"])
