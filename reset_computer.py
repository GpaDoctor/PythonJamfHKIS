from my_module import *

def reset(JPS_URL, JPS_USERNAME,JPS_PASSWORD):
	# Connect to Jemf

        
    with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:
        full_name_list =[]
        username_list = [] 
        serialnumber_list = []
        for i in shared.excel_data:
            full_name_list.append(str(i[2]) + " " + str(i[3]))
            fullname_array = np.array(full_name_list)
            username_list.append(str(i[1]))
            username_array = np.array(username_list)
            serialnumber_list.append(str(i[-1]))
            serialnumber_array = np.array(serialnumber_list)
        fullname_array = str(fullname_array).strip("[]")
        username_array = str(username_array).strip("[]")
        serialnumber_array = str(serialnumber_array).strip("[]")

    try:
        classic.delete_script(name="local_user_account_creation")
    except Exception as e:
        print(f"Failed to delete script: {e}")
        print("Creating a NEW one...")
        
    with Pro(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as pro:
        pro.create_script(
            {
                "name": "local_user_account_creation",
                "info": "Create a local user account.",
                "notes": "",
                "priority": "AFTER",
                "categoryId": "1",
                "categoryName": "Developer Tools",
                "parameter4": "1",
                "parameter5": "2",
                "parameter6": "3",
                "parameter7": "4",
                "parameter8": "5",
                "parameter9": "6",
                "parameter10": "7",
                "parameter11": "8",
                "osRequirements": "",
                "scriptContents": 
                """
                #!/bin/bash

                # Define an array of account names, full names, and serial numbers
                account_names=(testing)
                full_names=(test)
                serial_numbers=(FVFCW108P3YV)

                # Loop through the array and create the user account on each computer
                for (( i=0; i<${#account_names[@]}; i++ )); do
                    # Get the serial number of the computer
                    actual_serial_number=$(system_profiler SPHardwareDataType | awk '/Serial/ {print $4}')
                    
                    # Check if the serial number of the computer matches the desired serial number
                    if [ "$actual_serial_number" == "${serial_numbers[$i]}" ]; then
                        # Set the default password for the user account
                        default_password="Hkis1234"
                        
                        # Create the user account with the specified full name, account name, and default password
                        sysadminctl -addUser "${account_names[$i]}" -fullName "${full_names[$i]}" -password "$default_password"
                        
                        # Add the user account to the admin group
                        dseditgroup -o edit -a "${account_names[$i]}" -t user admin
                        
                        # Set the default user shell to bash
                        dscl . -create /Users/"${account_names[$i]}" UserShell /bin/bash
                        
                        # Display a message indicating that the account has been created
                        echo "User account created for serial number ${serial_numbers[$i]} with name ${computer_name[$i]}."
                    else
                        # Display a message indicating that the script did not run because the serial number did not match
                        echo "This script is not intended to run on this computer."
                    fi
                    done
                """ 
                                    
                }
            )
                    # % (username_array, fullname_array, serialnumber_array)

    try:
        classic.delete_policy(name="local_user_account_creation_trial")
    except Exception as e:
        print(f"Failed to delete policy: {e}")
        print("Creating a NEW one...")

    

    classic.create_policy(
        """
        <policy>
            <general>
                <name>local_user_account_creation_trial</name>
                <enabled>true</enabled>
                <trigger>string</trigger>
                <trigger_checkin>false</trigger_checkin>
                <trigger_enrollment_complete>true</trigger_enrollment_complete>
                <trigger_login>true</trigger_login>
                <trigger_logout>false</trigger_logout>
                <trigger_network_state_changed>false</trigger_network_state_changed>
                <trigger_startup>true</trigger_startup>
                <frequency>Ongoing</frequency>
                <location_user_only>false</location_user_only>
                <target_drive>/</target_drive>
                <offline>false</offline>
                <category>
                    <id>-1</id>
                    <name>Unknown</name>
                </category>
                <network_limitations>
                    <minimum_network_connection>No Minimum</minimum_network_connection>
                    <any_ip_address>true</any_ip_address>
                </network_limitations>
                <network_requirements>Any</network_requirements>
                <site>
                    <id>-1</id>
                    <name>None</name>
                </site>
            </general>
        </policy>
        """, 0
    )
    x = classic.get_policy(name="local_user_account_creation_trial")

    pprint(x)
    with open('output.txt', 'w') as f:
        f.write(str(x))




    exit()
    f = input("Press ENTER to continue...")

    with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:

        for i in shared.excel_data:

            SerialNumber = i[-1]	# *
            try:
                for_the_managemenent_id = classic.get_computer(serialnumber=SerialNumber)['computer']['general']['id']
                # x = classic.get_computer(serialnumber=SerialNumber)
                # with open('output.txt', 'w') as f:
                #     f.write(str(x))
                # print(for_the_managemenent_id)

            except Exception as e:
                print(f"Error retrieving device {SerialNumber}: {e}")
                shared.missing_computers.append(SerialNumber)
                # continue
            # try:
            #     x = classic.get_advanced_computer_search(id=12556)
            #     with open('output.txt', 'w') as f:
            #         f.write(str(x))

            # except Exception as e:
            #     print(f"Error retrieving device {SerialNumber}: {e}")
            #     shared.missing_computers.append(SerialNumber)
            #     # continue

            

            with Pro(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as pro:
                # the endpoint actually have a problem. This has to be updated in the pro.py file
                # command click on the pro.create_mdm_command to see the pro.py file
                # change the endpoint to the desired endpoint in this case endpoint = "/api/preview/mdm/commands"
                # save the pro.py file and run the script
                # the json dict for the parameter can be generated in the jamf classic api link
                # simply go to the corresponding api, fill in the parameters, in language click on Python copy the dictionary under payload = ...
                # The management id can be found under the inventory, general, Jamf Pro Management ID: ...

                # pro.create_mdm_command(
                #     {
                #     "commandData": {
                #         "commandType": "SETTINGS",
                #         "deviceName": "THIS IS ONE OF THE BEST DEVICES IN THE WORLD"
                #     },
                #     "clientData": [
                #         {
                #         "managementId": "4d7203c7-6043-4dae-8341-265768a15e5f"
                #         }
                #     ]
                #     }
                # )
                # pro.create_mdm_command(
                #     {
                #     "commandData": {
                #         "commandType": "RESTART_DEVICE",
                #         "rebuildKernelCache": False
                #     },
                #     "clientData": [
                #         {
                #         "managementId": "4d7203c7-6043-4dae-8341-265768a15e5f"
                #         }
                #     ]
                #     }
                # )

                #leave this for now, since testing the update requires downgrading the macos
                    # pro.create_managed_software_updates_plan(

                    # {
                    #     "devices": [
                    #         {
                    #             "objectType": "COMPUTER",
                    #             "deviceId": for_the_managemenent_id
                    #         }
                    #     ],
                    #     "config": {
                    #         "updateAction": "DOWNLOAD_INSTALL_RESTART",
                    #         "versionType": "LATEST_MAJOR",
                    #         "specificVersion": "NO_SPECIFIC_VERSION"
                    #     }
                    # }
                    # )
                


                    try:
                        management_id =  pro.get_computer_inventory(for_the_managemenent_id)['general']['managementId']
                        print(management_id)
                    except Exception as e:
                        print(f"Error retrieving device {SerialNumber}: {e}")
                        shared.missing_computers.append(SerialNumber)
                        # continue

                    pro.create_mdm_command(
                                    {
                            "commandData": {
                                "commandType": "ERASE_DEVICE",
                                "returnToService": {
                                    "enabled": True,
                                    "mdmProfileData": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHBsaXN0IFBVQkxJQyAiLS8vQXBwbGUvL0RURCBQTElTVCAxLjAvL0VOIiAiaHR0cDovL3d3dy5hcHBsZS5jb20vRFREcy9Qcm9wZXJ0eUxpc3QtMS4wLmR0ZCI+CjxwbGlzdCB2ZXJzaW9uPSIxIj4KICA8ZGljdD4KICAgIDxrZXk+UGF5bG9hZFVVSUQ8L2tleT4KICAgIDxzdHJpbmc+QzgwQkUxQUYtRTdDNC00MUY4LTg3QTEtMzUxQTFFNUNFNDVGPC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWRUeXBlPC9rZXk+CiAgICA8c3RyaW5nPkNvbmZpZ3VyYXRpb248L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZE9yZ2FuaXphdGlvbjwva2V5PgogICAgPHN0cmluZz5Ib25nIEtvbmcgSW50ZXJuYXRpb25hbCBTY2hvb2w8L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZElkZW50aWZpZXI8L2tleT4KICAgIDxzdHJpbmc+QzgwQkUxQUYtRTdDNC00MUY4LTg3QTEtMzUxQTFFNUNFNDVGPC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWREaXNwbGF5TmFtZTwva2V5PgogICAgPHN0cmluZz5IS0lTU0hBUkVEIFdpRmk8L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZERlc2NyaXB0aW9uPC9rZXk+CiAgICA8c3RyaW5nLz4KICAgIDxrZXk+UGF5bG9hZFZlcnNpb248L2tleT4KICAgIDxpbnRlZ2VyPjE8L2ludGVnZXI+CiAgICA8a2V5PlBheWxvYWRFbmFibGVkPC9rZXk+CiAgICA8dHJ1ZS8+CiAgICA8a2V5PlBheWxvYWRSZW1vdmFsRGlzYWxsb3dlZDwva2V5PgogICAgPHRydWUvPgogICAgPGtleT5QYXlsb2FkU2NvcGU8L2tleT4KICAgIDxzdHJpbmc+U3lzdGVtPC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWRDb250ZW50PC9rZXk+CiAgICA8YXJyYXk+CiAgICAgIDxkaWN0PgogICAgICAgIDxrZXk+UGF5bG9hZFVVSUQ8L2tleT4KICAgICAgICA8c3RyaW5nPjJFRjI4QzUzLTA2MEUtNEFGNi04NDhGLTE2Mjg0QTM3MDJDRTwvc3RyaW5nPgogICAgICAgIDxrZXk+UGF5bG9hZFR5cGU8L2tleT4KICAgICAgICA8c3RyaW5nPmNvbS5hcHBsZS53aWZpLm1hbmFnZWQ8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWRPcmdhbml6YXRpb248L2tleT4KICAgICAgICA8c3RyaW5nPkhvbmcgS29uZyBJbnRlcm5hdGlvbmFsIFNjaG9vbDwvc3RyaW5nPgogICAgICAgIDxrZXk+UGF5bG9hZElkZW50aWZpZXI8L2tleT4KICAgICAgICA8c3RyaW5nPjJFRjI4QzUzLTA2MEUtNEFGNi04NDhGLTE2Mjg0QTM3MDJDRTwvc3RyaW5nPgogICAgICAgIDxrZXk+UGF5bG9hZERpc3BsYXlOYW1lPC9rZXk+CiAgICAgICAgPHN0cmluZz5XaUZpIChIS0lTU0hBUkVEKTwvc3RyaW5nPgogICAgICAgIDxrZXk+UGF5bG9hZERlc2NyaXB0aW9uPC9rZXk+CiAgICAgICAgPHN0cmluZy8+CiAgICAgICAgPGtleT5QYXlsb2FkVmVyc2lvbjwva2V5PgogICAgICAgIDxpbnRlZ2VyPjE8L2ludGVnZXI+CiAgICAgICAgPGtleT5QYXlsb2FkRW5hYmxlZDwva2V5PgogICAgICAgIDx0cnVlLz4KICAgICAgICA8a2V5PkhJRERFTl9ORVRXT1JLPC9rZXk+CiAgICAgICAgPGZhbHNlLz4KICAgICAgICA8a2V5PlBhc3N3b3JkPC9rZXk+CiAgICAgICAgPHN0cmluZz4xQG10aGVXQGxydXM8L3N0cmluZz4KICAgICAgICA8a2V5PkVuY3J5cHRpb25UeXBlPC9rZXk+CiAgICAgICAgPHN0cmluZz5XUEE8L3N0cmluZz4KICAgICAgICA8a2V5PkF1dG9Kb2luPC9rZXk+CiAgICAgICAgPHRydWUvPgogICAgICAgIDxrZXk+Q2FwdGl2ZUJ5cGFzczwva2V5PgogICAgICAgIDxmYWxzZS8+CiAgICAgICAgPGtleT5Qcm94eVR5cGU8L2tleT4KICAgICAgICA8c3RyaW5nPk5vbmU8L3N0cmluZz4KICAgICAgICA8a2V5PlNldHVwTW9kZXM8L2tleT4KICAgICAgICA8YXJyYXkvPgogICAgICAgIDxrZXk+U1NJRF9TVFI8L2tleT4KICAgICAgICA8c3RyaW5nPkhLSVNTSEFSRUQ8L3N0cmluZz4KICAgICAgICA8a2V5PkludGVyZmFjZTwva2V5PgogICAgICAgIDxzdHJpbmc+QnVpbHRJbldpcmVsZXNzPC9zdHJpbmc+CiAgICAgIDwvZGljdD4KICAgIDwvYXJyYXk+CiAgPC9kaWN0Pgo8L3BsaXN0Pgo=",
                                    "wifiProfileData": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHBsaXN0IFBVQkxJQyAiLS8vQXBwbGUvL0RURCBQTElTVCAxLjAvL0VOIiAiaHR0cDovL3d3dy5hcHBsZS5jb20vRFREcy9Qcm9wZXJ0eUxpc3QtMS4wLmR0ZCI+CjxwbGlzdCB2ZXJzaW9uPSIxIj4KICA8ZGljdD4KICAgIDxrZXk+UGF5bG9hZFVVSUQ8L2tleT4KICAgIDxzdHJpbmc+QzgwQkUxQUYtRTdDNC00MUY4LTg3QTEtMzUxQTFFNUNFNDVGPC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWRUeXBlPC9rZXk+CiAgICA8c3RyaW5nPkNvbmZpZ3VyYXRpb248L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZE9yZ2FuaXphdGlvbjwva2V5PgogICAgPHN0cmluZz5Ib25nIEtvbmcgSW50ZXJuYXRpb25hbCBTY2hvb2w8L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZElkZW50aWZpZXI8L2tleT4KICAgIDxzdHJpbmc+QzgwQkUxQUYtRTdDNC00MUY4LTg3QTEtMzUxQTFFNUNFNDVGPC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWREaXNwbGF5TmFtZTwva2V5PgogICAgPHN0cmluZz5IS0lTU0hBUkVEIFdpRmk8L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZERlc2NyaXB0aW9uPC9rZXk+CiAgICA8c3RyaW5nLz4KICAgIDxrZXk+UGF5bG9hZFZlcnNpb248L2tleT4KICAgIDxpbnRlZ2VyPjE8L2ludGVnZXI+CiAgICA8a2V5PlBheWxvYWRFbmFibGVkPC9rZXk+CiAgICA8dHJ1ZS8+CiAgICA8a2V5PlBheWxvYWRSZW1vdmFsRGlzYWxsb3dlZDwva2V5PgogICAgPHRydWUvPgogICAgPGtleT5QYXlsb2FkU2NvcGU8L2tleT4KICAgIDxzdHJpbmc+U3lzdGVtPC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWRDb250ZW50PC9rZXk+CiAgICA8YXJyYXk+CiAgICAgIDxkaWN0PgogICAgICAgIDxrZXk+UGF5bG9hZFVVSUQ8L2tleT4KICAgICAgICA8c3RyaW5nPjJFRjI4QzUzLTA2MEUtNEFGNi04NDhGLTE2Mjg0QTM3MDJDRTwvc3RyaW5nPgogICAgICAgIDxrZXk+UGF5bG9hZFR5cGU8L2tleT4KICAgICAgICA8c3RyaW5nPmNvbS5hcHBsZS53aWZpLm1hbmFnZWQ8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWRPcmdhbml6YXRpb248L2tleT4KICAgICAgICA8c3RyaW5nPkhvbmcgS29uZyBJbnRlcm5hdGlvbmFsIFNjaG9vbDwvc3RyaW5nPgogICAgICAgIDxrZXk+UGF5bG9hZElkZW50aWZpZXI8L2tleT4KICAgICAgICA8c3RyaW5nPjJFRjI4QzUzLTA2MEUtNEFGNi04NDhGLTE2Mjg0QTM3MDJDRTwvc3RyaW5nPgogICAgICAgIDxrZXk+UGF5bG9hZERpc3BsYXlOYW1lPC9rZXk+CiAgICAgICAgPHN0cmluZz5XaUZpIChIS0lTU0hBUkVEKTwvc3RyaW5nPgogICAgICAgIDxrZXk+UGF5bG9hZERlc2NyaXB0aW9uPC9rZXk+CiAgICAgICAgPHN0cmluZy8+CiAgICAgICAgPGtleT5QYXlsb2FkVmVyc2lvbjwva2V5PgogICAgICAgIDxpbnRlZ2VyPjE8L2ludGVnZXI+CiAgICAgICAgPGtleT5QYXlsb2FkRW5hYmxlZDwva2V5PgogICAgICAgIDx0cnVlLz4KICAgICAgICA8a2V5PkhJRERFTl9ORVRXT1JLPC9rZXk+CiAgICAgICAgPGZhbHNlLz4KICAgICAgICA8a2V5PlBhc3N3b3JkPC9rZXk+CiAgICAgICAgPHN0cmluZz4xQG10aGVXQGxydXM8L3N0cmluZz4KICAgICAgICA8a2V5PkVuY3J5cHRpb25UeXBlPC9rZXk+CiAgICAgICAgPHN0cmluZz5XUEE8L3N0cmluZz4KICAgICAgICA8a2V5PkF1dG9Kb2luPC9rZXk+CiAgICAgICAgPHRydWUvPgogICAgICAgIDxrZXk+Q2FwdGl2ZUJ5cGFzczwva2V5PgogICAgICAgIDxmYWxzZS8+CiAgICAgICAgPGtleT5Qcm94eVR5cGU8L2tleT4KICAgICAgICA8c3RyaW5nPk5vbmU8L3N0cmluZz4KICAgICAgICA8a2V5PlNldHVwTW9kZXM8L2tleT4KICAgICAgICA8YXJyYXkvPgogICAgICAgIDxrZXk+U1NJRF9TVFI8L2tleT4KICAgICAgICA8c3RyaW5nPkhLSVNTSEFSRUQ8L3N0cmluZz4KICAgICAgICA8a2V5PkludGVyZmFjZTwva2V5PgogICAgICAgIDxzdHJpbmc+QnVpbHRJbldpcmVsZXNzPC9zdHJpbmc+CiAgICAgIDwvZGljdD4KICAgIDwvYXJyYXk+CiAgPC9kaWN0Pgo8L3BsaXN0Pgo="
                                },
                                "pin": "123456"
                            },
                            "clientData": [{ "managementId": management_id }]
                        }
                    )

                    
                    break
            
                    






                

            

        