from os import environ

from jps_api_wrapper.classic import Classic
from pprint import pprint

JPS_URL = "https://jss.hkis.edu.hk:8443/"
JPS_USERNAME = environ.get("JPS_USERNAME")
JPS_PASSWORD = environ.get("JPS_PASSWORD")

with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:
	mobile_devices = classic.get_mobile_devices()	
	pprint(mobile_devices)
