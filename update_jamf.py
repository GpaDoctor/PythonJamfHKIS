from my_module import *


def Execute(JPS_URL, JPS_USERNAME,JPS_PASSWORD):

	# Connect to Jamf
	with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:

		#UserName = []

		for i in shared.excel_data:
			# Declare variables
			# Information has to be filled in first before runnning the below code. Please fill in *
			# The following information will later be drawn directly from a accdb file or a csv file for automation purposes
			UserInformation = []

			# UserName is i[0] in the excel file
			# UserName = i[0]					# *
			SerialNumber = i[-1]	# *
			# print(i)
			# print(f"Serial Number: {SerialNumber}")
			# continue
			# ComputerName = "This is amazinggggggg"	# *
			LocationInformation = ["Email Address", "Username", "Preferred", "Surname", "Deparment Code", "Department", "Business Title", "Campus", "Telephone", "Room", "Inventory Number"]

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
			try:
				DeviceNeedUpdating = classic.get_computer(serialnumber=SerialNumber)
			except Exception as e:
				print(f"Error retrieving device {SerialNumber}: {e}")
				shared.missing_computers.append(SerialNumber)
				continue

			print("Device Information is shown below")
			pprint(DeviceNeedUpdating['computer']["location"])			#use nested list to find the information needed
			print("\n")


			# # To get user information from Jamf
			# try:
			# 	GetUserInfo = classic.get_user(name=UserName, data_type="json")
			# 	# Process GetUserInfo as it's successfully retrieved
			# except Exception as e:  # Replace Exception with a more specific exception if possible
			# 	# Handle the error, e.g., log it or append UserName to missing_people
			# 	print(f"Error retrieving user {UserName}: {e}")
			# 	shared.missing_people.append(UserName)
			# 	continue

			# print("User Information is shown below")
			# for j_index, j_value in enumerate(LocationInformation[0:4]):
			# 	UserInformation.append(GetUserInfo['user'][j_value])			#use nested list to find what the information and append it to list
			# 	print(f"{j_value}: {UserInformation[-1]}")
			# 	#print the newly appened information
			# # print(UserInformation)
			# # exit()
			# for j_index, j_value in enumerate(LocationInformation[4:]):
			# 	UserInformation.append(i[j_index+1])
			# 	print(f"{LocationInformation[4+j_index]}: {UserInformation[-1]}")
			
			# # print(UserInformation)
			# # exit()

			# JUST GET THE DATA FROM THE EXCEL FILE AND UPDATE THE JAMF
			for j_index, j_value in enumerate(LocationInformation):
				UserInformation.append(str(i[j_index]))
				print(f"{j_value}: {UserInformation[-1]}")
			full_name = str(UserInformation[2]) + " " + str(UserInformation[3])
			name_for_computer = str(UserInformation[4]) + " LTOP " + str(UserInformation[10])
			print(name_for_computer)



			print("\n")
			time.sleep(1)


			# Update computer name 
			classic.update_computer(
				f"""
				<computer>
					<general>
					<name>{name_for_computer}</name>
					</general>
				</computer>
				""",													#Xml are in "" therefore use f string and use {} to include variables
				serialnumber=SerialNumber
			)

			print("Computer Name has been updated.")
			print("\n")
			time.sleep(1)

			# Modify the UserInformation processing to print each info during the loop
			for index, info in enumerate(UserInformation):
				info_str = str(info)  # Convert info to string to prevent AttributeError
				escaped_info = saxutils.escape(info_str)
				UserInformation[index] = escaped_info
				print(f"Escaped Info {index}: {escaped_info}")  # Print each escaped info


			try:
				# Call the classic.update_computer function with the provided XML data and serial number
				classic.update_computer(
					f"""
					<computer>
						<general/>
						<location>
							<username>{UserInformation[1]}</username>
							<realname>{full_name}</realname>
							<real_name/>
							<email_address>{UserInformation[0]}</email_address>
							<position>{UserInformation[6]}</position>
							<phone>{UserInformation[8]}</phone>
							<department>{UserInformation[4]}</department>
							<building>{UserInformation[7]}</building>
							<room>{UserInformation[9]}</room>
						</location>
					</computer>
					""",
					serialnumber=SerialNumber
				)
			except Exception as e:
				print(f"Failed to update everything: {e}")
				shared.error_in_updating.append(UserInformation[1])
				try:
					# Second try: Attempt to update only the department
					classic.update_computer(
						f"""
						<computer>
							<general/>
							<location>
								<username>{UserInformation[1]}</username>
								<realname>{full_name}</realname>
								<real_name/>
								<email_address>{UserInformation[0]}</email_address>
								<position>{UserInformation[6]}</position>
								<phone>{UserInformation[8]}</phone>
								<phone_number>{UserInformation[8]}</phone_number>
								<department>{UserInformation[4]}</department>
								<building></building>
								<room>{UserInformation[9]}</room>
							</location>
						</computer>
						""",
						serialnumber=SerialNumber
					)
				except Exception as e:
					print(f"Failed to update department: {e}")
					try:
						# Third try: Attempt to update only the building
						classic.update_computer(
							f"""
							<computer>
								<general/>
								<location>
									<username>{UserInformation[1]}</username>
									<realname>{full_name}</realname>
									<real_name/>
									<email_address>{UserInformation[0]}</email_address>
									<position>{UserInformation[6]}</position>
									<phone>{UserInformation[8]}</phone>
									<department></department>
									<building>{UserInformation[7]}</building>
									<room>{UserInformation[9]}</room>
								</location>
							</computer>
							""",
							serialnumber=SerialNumber
						)
					except Exception as e:
						print(f"Failed to update building: {e}")
						# Final attempt: Update everything except department and building
						classic.update_computer(
							f"""
							<computer>
								<general/>
								<location>
									<username>{UserInformation[1]}</username>
									<realname>{full_name}</realname>
									<real_name/>
									<email_address>{UserInformation[0]}</email_address>
									<position>{UserInformation[6]}</position>
									<phone>{UserInformation[8]}</phone>
									<department></department>
									<building></building>
									<room>{UserInformation[9]}</room>
								</location>
							</computer>
							""",
							serialnumber=SerialNumber
						)
			
			# f = input("Press Enter to continue...")

		print(f"Missing Computers in System: {shared.missing_computers}")
		# print(f"Missing People in System: {shared.missing_people}")
		print(f"There is a error when updating these people: {shared.error_in_updating}")

		


	



	
	