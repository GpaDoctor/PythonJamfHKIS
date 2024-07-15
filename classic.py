from os import environ

from jps_api_wrapper.classic import Classic
from pprint import pprint

import time
import json
import xml
import requests
import xml.etree.ElementTree as ET


JPS_URL = "https://jss.hkis.edu.hk:8443/"
JPS_USERNAME = environ.get("JPS_USERNAME")
JPS_PASSWORD = environ.get("JPS_PASSWORD")

with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:
	# The following is all for testing

	#mobile_devices = classic.get_mobile_devices()	
	#pprint(mobile_devices)

	# classic.create_computer_group(
	# 	"""
	# 	<computer_group>
    # 		<name>ThisIsForTesting</name>
    # 		<is_smart>false</is_smart>
    # 		<site>
    #    		<id>-1</id>
    #    		<name>None</name>
    # 	</site>
    # 	</computer_group>
	# 	""", 
	# 	0
	# )

	# classic.delete_computer_group(None, "ThisIsForTesting")

	#testing = classic.get_computer_group(None,"Can delete from Jamf")
	#pprint(testing)


	#DeviceNeedUpdating = classic.get_computer(None, None, None, "FVFCW0Z4P3YV", None)["Computer Name"]

	GetUserInfo = classic.get_user(None,"deswong",None,"json")



	
	# classic.update_computer(
	# 	"""
	# 	<computer>
    # 		<general>
    #     	<name>This is amazinggggggg</name>
	# 		</general>
	# 	</computer>
	# 	""",
	# 	None, None, None, "FVFCW0Z4P3YV", None
	# )

	# classic.get_advanced_user_search

	pprint((GetUserInfo['user']['full_name'],
		 GetUserInfo['user']['email'],
		 GetUserInfo['user']['phone_number'],
		 GetUserInfo['user']['position'] 
		 ))


	time.sleep(5)



	
	