# Nebula-Python-SDK
An SDK for managing [nebula](http://nebula.readthedocs.io/en/latest/) via python.

translates all of Nebula [API](http://nebula.readthedocs.io/en/latest/api/) calls to something more pythonic.

# How To Use
```python
# Install from PyPi
pip install NebulaPythonSDK

# Load API wrapper from library
from NebulaPythonSDK import Nebula

# Create API object.
# port defaults to 80 and protocol defaults to http if not set
connection = Nebula(username="your_nebula_user", password="your_nebula_pass", host="nebula.example.com",port=80, protocol="http")

# List apps
app_list = connection.list_apps()

# List app info
app_config = connection.list_app_info("app_name")

# Create app
app_conf = {
    "containers_per_cpu": 8,
    "env_vars": {
        "test": "blabla",
        "test3t2t32": "tesg4ehgee"
    },
    "docker_ulimits": [],
    "network_mode": "bridge",
    "running": True,
    "containers_per": {
        "cpu": 6
    },
    "starting_ports": [
        {
            "81": 80
        }
    ],
    "docker_image": "httpd"
}
connection.create_app("app_name", app_conf)
```