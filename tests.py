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
        if reply["status_code"] != 200:
            raise Exception("check /status failed")
