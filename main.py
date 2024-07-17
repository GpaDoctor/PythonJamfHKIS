from my_module import *

JPS_URL = "https://jss.hkis.edu.hk:8443/"
JPS_USERNAME = environ.get("JPS_USERNAME")
JPS_PASSWORD = environ.get("JPS_PASSWORD")

UpdateJemf.Execute(JPS_URL, JPS_USERNAME,JPS_PASSWORD)
