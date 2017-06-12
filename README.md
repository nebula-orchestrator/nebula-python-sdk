# Nebula-Python-SDK
An SDK for managing [nebula](http://nebula.readthedocs.io/en/latest/) via python.

translates all of Nebula [API](http://nebula.readthedocs.io/en/latest/api/) calls to something more pythonic.

# How To Use
```python
# install from PyPi
pip install NebulaPythonSDK

# Load API wrapper from library
from NebulaPythonSDK import Nebula

# Create API object.
connection = Nebula(username="your_nebula_user", password="your_nebula_pass", host="nebula.example.com", protocol="http")

# list apps
app_list = connection.list_apps()

# list app info
app_config = connection.list_app_info("app_name")

# create app
app_conf = {
    "containers_per_cpu": 8,
    "app_name": "test123",
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
    "_id": {
        "$oid": "581a0e297a3a0f000aa1012d"
    },
    "docker_image": "httpd"
}
connection.create_app("app_name", app_conf)
```