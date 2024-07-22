from my_module import *


def Execute(JPS_URL, JPS_USERNAME,JPS_PASSWORD):

	# Connect to Jemf
	with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:

		#UserName = []

		for i in shared.excel_data:
			# Declare variables
			#information has to be filled in first before runnning the below code. Please fill in *
			# The following information will later be drawn directly from a accdb file or a csv file for automation purposes
			UserInformation = []

			# UserName is i[0] in the excel file
			UserName = i[0]					# *
			SerialNumber = "FVFCW0Z4P3YV"	# *
			# ComputerName = "This is amazinggggggg"	# *
			LocationInformation =["full_name","email", "phone_number", "position", "Department", "Building", "Room" ]

			# Assign variables
			
			# UserName.append(i[0])

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
			DeviceNeedUpdating = classic.get_computer(serialnumber=SerialNumber)

			print("Device Information is shown below")
			pprint(DeviceNeedUpdating['computer']["location"])			#use nested list to find the information needed
			print("\n")


			# To get user information from Jemf
			GetUserInfo = classic.get_user(name=UserName, data_type="json")	#specify the file you want at the end, either json or xml

			print("User Information is shown below")
			for j_index, j_value in enumerate(LocationInformation[0:4]):
				UserInformation.append(GetUserInfo['user'][j_value])			#use nested list to find what the information and append it to list
				print(f"{j_value}: {UserInformation[-1]}")
				#print the newly appened information
			# print(UserInformation)
			# exit()
			for j_index, j_value in enumerate(LocationInformation[4:]):
				UserInformation.append(i[j_index+1])
				print(f"{LocationInformation[4+j_index]}: {UserInformation[-1]}")
			
			# print(UserInformation)
			# exit()


			print("\n")
			time.sleep(1)


			# Update computer name 
			classic.update_computer(
				f"""
				<computer>
					<general>
					<name>{UserName} Computer</name>
					</general>
				</computer>
				""",													#Xml are in "" therefore use f string and use {} to include variables
				serialnumber=SerialNumber
			)

			print("Computer Name has been updated.")
			print("\n")
			time.sleep(1)

			print("Updating Computer User and Location")
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
						<department>{UserInformation[4]}</department>
						<building>{UserInformation[5]}</building>
						<room>{UserInformation[6]}</room>
					</location>
				</computer>
				""",													#same as before xml file in f string, {} to declare a variable
				serialnumber=SerialNumber
			)

			print("Computer User and Location has been updated.")
			test = input("Press Enter to Continue")
	



	
	