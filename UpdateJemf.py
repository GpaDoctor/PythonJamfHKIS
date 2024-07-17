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
	# Declare variables
	#information has to be filled in first before runnning the below code. Please fill in *
	# The following information will later be drawn directly from a accdb file or a csv file for automation purposes
	UserInformation = []
	UserName = "deswong"					# *
	SerialNumber = "FVFCW0Z4P3YV"			# *
	ComputerName = "This is amazinggggggg"	# *
	LocationInformation =["full_name","email", "phone_number", "position" ]


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


	#Get information of the device
	DeviceNeedUpdating = classic.get_computer(None, None, None, SerialNumber, None, None )

	pprint(DeviceNeedUpdating['computer']["location"])			#use nested list to find the information needed
	print("\n")


	# Update computer name 
	classic.update_computer(
		f"""
		<computer>
			<general>
			<name>{ComputerName}</name>
			</general>
		</computer>
		""",													#Xml are in "" therefore use f string and use {} to include variables
		None, None, None, SerialNumber, None
	)

	print("Computer Name has been updated.")
	print("\n")
	time.sleep(1)

	
	# To get user information from Jemf
	GetUserInfo = classic.get_user(None,UserName,None,"json")	#specify the file you want at the end, either json or xml

	print("User Information is shown below")
	for i in LocationInformation:
		UserInformation.append(GetUserInfo['user'][i])			#use nested list to find what the information and append it to list
		print(f"{i}: {UserInformation[-1]}")					#print the newly appened information
	print("\n")
	time.sleep(1)


	# Update Computer User and Location
	classic.update_computer(
		f"""
		<computer>
			<general/>
			<location>
				<username>{UserName}</username>
				<realname>{UserInformation[0]}</realname>
				<real_name/>
				<email_address>{UserInformation[1]}</email_address>
				<position>{UserInformation[3]}</position>
				<phone/>
				<phone_number>{UserInformation[2]}</phone_number>
				<department/>
				<building/>
				<room/>
			</location>
		</computer>
		""",													#same as before xml file in f string, {} to declare a variable
		None, None, None, SerialNumber, None
	)

	



	
	