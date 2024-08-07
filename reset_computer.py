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

    # x = classic.get_policy(name="somehow", data_type="xml")
    # with open("output.txt", "w") as f:
    #     f.write(str(x))
    # exit()

    # x = classic.get_policy(name="printer_driver_creation",data_type="xml")
    # print(x)
    # with open("output.txt", "w") as f:
    #     f.write(str(x))
    # exit() 
    

    # For deleting the policy
    try:
        classic.delete_policy(name="local_user_account_creation_trial")
    except Exception as e:
        print(f"Failed to delete policy: {e}")
        print("Ignore")

    try: 
        classic.delete_policy(name="printer_driver_creation_trial")
    except Exception as e:
        print(f"Failed to delete policy: {e}")
        print("Ignore")

    # For deleting the script
    try:
        classic.delete_script(name="local_user_account_creation")
    except Exception as e:
        print(f"Failed to delete script: {e}")
        print("Creating a NEW one...")

    try:
        classic.delete_script(name="printer_driver_creation")
    except Exception as e:
        print(f"Failed to delete script: {e}")
        print("Creating a NEW one...")

    # For creating the script

    # For your reference % syntax for string formatting is outdate. This is not recommended as it will result in type error when used in complex formatting.
    # Instead use .format for complex formatting
    # To replace a abundant amount of {} with {{}}. Use cmd + shift + h in vs code. and replace all.
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
                account_names=(%s)
                full_names=(%s)
                serial_numbers=(%s)

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
                """ %(username_array, fullname_array, serialnumber_array)                                 
                }
            )
        
        pro.create_script(
            {
                "name": "printer_driver_creation",
                "info": "Create a printer driver.",
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
                # Define an array of account names, and serial numbers
                account_names=({0})
                serial_numbers=({1})

                # Get the serial number of the computer
                actual_serial_number=$(system_profiler SPHardwareDataType | awk '/Serial/ {{print $4}}')

                # Loop through the array and create the user account on each computer
                for (( i=0; i<${{#account_names[@]}}; i++ )); do
                    if [ "$actual_serial_number" == "${{serial_numbers[$i]}}" ]; then
                        echo "INFO: Serial number matches for ${{account_names[$i]}}"

                        # Define printer variables for Tai Tam
                        TTURL="10.2.0.107"
                        TTPrinterName="TT_PRINTER_COLOR_PS"
                        TTDescription="TTPRINTER"

                        # Define printer variables for Repulse Bay
                        RBURL="10.1.0.107"
                        RBPrinterName="RB_PRINTER_COLOR_PS"
                        RBDescription="RBPRINTER"

                        # Ensure PPD file exists
                        hkisPPD="/Library/Printers/PPDs/Contents/Resources/Booklet.ppd"
                        if [ -f "$hkisPPD" ]; then
                            # Get the username of the currently logged-in user
                            userID=`stat -f "%Su" /dev/console`

                            # Construct Printer URL and Description for Tai Tam
                            TTPrinterURL="$userID@$TTURL"
                            TTPrinterDescription="${{account_names[$i]}}@TTprinter"
                            echo "INFO: The Tai Tam Printer URL is $TTPrinterURL"

                            # Create the Tai Tam printer
                            TTPrinterString="lpadmin -p $TTPrinterDescription -L TT -E -v lpd://$TTPrinterURL/$TTPrinterName -P \"$hkisPPD\" -o printer-is-shared=false -o FXColorMode=Black -o Duplex=DuplexNoTumble -o PageSize=A4"
                            echo "INFO: The Tai Tam PrinterString is '$TTPrinterString'"
                            lpadmin -p $TTPrinterDescription -L TT -E -v lpd://$TTPrinterURL/$TTPrinterName -P "${{hkisPPD}}" -o printer-is-shared=false -o FXColorMode=Black -o Duplex=DuplexNoTumble -o PageSize=A4

                            # Set printer settings for Tai Tam
                            TTPrinterSetting="lpadmin -p $TTPrinterDescription -o FXColorMode=Black -o Duplex=DuplexNoTumble -o PageSize=A4"
                            echo "INFO: The Tai Tam PrinterSettings are '$TTPrinterSetting'"
                            lpadmin -p $TTPrinterDescription -o FXColorMode=Black -o Duplex=DuplexNoTumble -o PageSize=A4

                            # Construct Printer URL and Description for Repulse Bay
                            RBPrinterURL="$userID@$RBURL"
                            RBPrinterDescription="${{account_names[$i]}}@RBprinter"
                            echo "INFO: The Repulse Bay Printer URL is $RBPrinterURL"

                            # Create the Repulse Bay printer
                            RBPrinterString="lpadmin -p $RBPrinterDescription -L RB -E -v lpd://$RBPrinterURL/$RBPrinterName -P \"$hkisPPD\" -o printer-is-shared=false -o FXColorMode=Black -o Duplex=DuplexNoTumble -o PageSize=A4"
                            echo "INFO: The Repulse Bay PrinterString is '$RBPrinterString'"
                            lpadmin -p $RBPrinterDescription -L RB -E -v lpd://$RBPrinterURL/$RBPrinterName -P "${{hkisPPD}}" -o printer-is-shared=false -o FXColorMode=Black -o Duplex=DuplexNoTumble -o PageSize=A4

                            # Set printer settings for Repulse Bay
                            RBPrinterSetting="lpadmin -p $RBPrinterDescription -o FXColorMode=Black -o Duplex=DuplexNoTumble -o PageSize=A4"
                            echo "INFO: The Repulse Bay PrinterSettings are '$RBPrinterSetting'"
                            lpadmin -p $RBPrinterDescription -o FXColorMode=Black -o Duplex=DuplexNoTumble -o PageSize=A4
                        else
                            echo "ERROR: Print Driver Not Found."
                        fi
                    else
                        echo "INFO: Serial number does not match for ${{account_names[$i]}}"
                    fi
                    done
                """.format(username_array,serialnumber_array)
            }
        )

    # For deleting the computer group
    try:
        classic.delete_computer_group(name="intended_for_local_user_account_creation_and_printer_driver_creation_trial")
    except Exception as e:
        print(f"Failed to delete computer group: {e}")
        print("Creating a NEW one...")
    time.sleep(1)
    
    # For creating the computer group
    classic.create_computer_group(
        """
        <computer_group>
            <name>intended_for_local_user_account_creation_and_printer_driver_creation_trial</name>
            <is_smart>false</is_smart>
            <site>
                <id>-1</id>
                <name>None</name>
            </site>
        </computer_group>
        """, id=0
    )

    for i in shared.excel_data:
        for_computer_group_id = classic.get_computer(serialnumber=i[-1])['computer']['general']['id']
        for_computer_group_name = classic.get_computer(serialnumber=i[-1])['computer']['general']['name']
        for_computer_group_mac_address = classic.get_computer(serialnumber=i[-1])['computer']['general']['mac_address']
        for_computer_group_alt_mac_address = classic.get_computer(serialnumber=i[-1])['computer']['general']['alt_mac_address']
        for_computer_group_serial_number = classic.get_computer(serialnumber=i[-1])['computer']['general']['serial_number']
        # print(for_computer_group_id)
        # print(for_computer_group_name) 
        # print(for_computer_group_mac_address)
        # print(for_computer_group_alt_mac_address)
        # print(for_computer_group_serial_number)
  
        classic.update_computer_group(
            data="""
                <computer_group>
                <computer_additions>
                    <computer>
                    <id>{0}</id>
                    <name>{1}</name>
                    <mac_address>{2}</mac_address>
                    <alt_mac_address>{3}</alt_mac_address>
                    <serial_number>{4}</serial_number>
                    </computer>
                </computer_additions>
                </computer_group>
                """.format(for_computer_group_id, for_computer_group_name, for_computer_group_mac_address, for_computer_group_alt_mac_address, for_computer_group_serial_number), name="intended_for_local_user_account_creation_and_printer_driver_creation_trial"
                )

    try:
        classic.delete_policy(name="local_user_account_creation_trial")
    except Exception as e:
        print(f"Failed to delete policy: {e}")
        print("Creating a NEW one...")

    try:
        classic.delete_policy(name="printer_driver_creation_trial")
    except Exception as e:
        print(f"Failed to delete policy: {e}")
        print("Creating a NEW one...")   

    # computer_id_list = []
    # computer_name_list = []
    # computer_udid_list = []
    
    # for i in shared.excel_data:
    #     computer_id_list.append(classic.get_computer(serialnumber=i[-1])['computer']['general']['id'])
    #     computer_name_list.append(classic.get_computer(serialnumber=i[-1])['computer']['general']['name'])
    #     computer_udid_list.append(classic.get_computer(serialnumber=i[-1])['computer']['general']['udid'])
    # print(computer_id_list)
    # print(computer_name_list)
    # print(computer_udid_list)
    # exit()

    # create a policy for local user account creation
    script_id = classic.get_script(name="local_user_account_creation")['script']['id']
    script_name = classic.get_script(name="local_user_account_creation")['script']['name']
    computer_group_id = classic.get_computer_group(name="intended_for_local_user_account_creation_and_printer_driver_creation_trial")['computer_group']['id']
    computer_group_name = classic.get_computer_group(name="intended_for_local_user_account_creation_and_printer_driver_creation_trial")['computer_group']['name']

    classic.create_policy(
        """
        <policy>
            <general>
                <id/>
                <name>local_user_account_creation_trial</name>
                <enabled>true</enabled>
                <trigger>EVENT</trigger>
                <trigger_checkin>false</trigger_checkin>
                <trigger_enrollment_complete>false</trigger_enrollment_complete>
                <trigger_login>false</trigger_login>
                <trigger_network_state_changed>false</trigger_network_state_changed>
                <trigger_startup>true</trigger_startup>
                <trigger_other/>
                <frequency>Ongoing</frequency>
                <retry_event>none</retry_event>
                <retry_attempts>-1</retry_attempts>
                <notify_on_each_failed_retry>false</notify_on_each_failed_retry>
                <location_user_only>false</location_user_only>
                <target_drive>/</target_drive>
                <offline>false</offline>
                <category>
                    <id>-1</id>
                    <name>No category assigned</name>
                </category>
                <date_time_limitations>
                    <activation_date/>
                    <activation_date_epoch>0</activation_date_epoch>
                    <activation_date_utc/>
                    <expiration_date/>
                    <expiration_date_epoch>0</expiration_date_epoch>
                    <expiration_date_utc/>
                    <no_execute_on/>
                    <no_execute_start/>
                    <no_execute_end/>
                </date_time_limitations>
                <network_limitations>
                    <minimum_network_connection>No Minimum</minimum_network_connection>
                    <any_ip_address>true</any_ip_address>
                    <network_segments/>
                </network_limitations>
                <override_default_settings>
                    <target_drive>/</target_drive>
                    <distribution_point>default</distribution_point>
                    <force_afp_smb>false</force_afp_smb>
                    <sus>default</sus>
                </override_default_settings>
                <network_requirements>Any</network_requirements>
                <site>
                    <id>-1</id>
                    <name>None</name>
                </site>
            </general>
            <scope>
                <all_computers>false</all_computers>
                <computers/>
                <computer_groups>
                    <computer_group>
                        <id>{0}</id>
                        <name>{1}</name>
                    </computer_group>
                </computer_groups>
                <buildings/>
                <departments/>
                <limit_to_users>
                    <user_groups/>
                </limit_to_users>
                <limitations>
                    <users/>
                    <user_groups/>
                    <network_segments/>
                    <ibeacons/>
                </limitations>
                <exclusions>
                    <computers/>
                    <computer_groups/>
                    <buildings/>
                    <departments/>
                    <users/>
                    <user_groups/>
                    <network_segments/>
                    <ibeacons/>
                </exclusions>
            </scope>
            <self_service>
                <use_for_self_service>false</use_for_self_service>
                <self_service_display_name/>
                <install_button_text>Install</install_button_text>
                <reinstall_button_text>Reinstall</reinstall_button_text>
                <self_service_description/>
                <force_users_to_view_description>false</force_users_to_view_description>
                <self_service_icon/>
                <feature_on_main_page>false</feature_on_main_page>
                <self_service_categories/>
                <notification>false</notification>
                <notification_type>Self Service</notification_type>
                <notification_subject>somehow</notification_subject>
                <notification_message/>
            </self_service>
            <package_configuration>
                <packages>
                    <size>0</size>
                </packages>
                <distribution_point>default</distribution_point>
            </package_configuration>
            <scripts>
                <size>1</size>
                <script>
                    <id>{2}</id>
                    <name>{3}</name>
                    <priority>After</priority>
                    <parameter4/>
                    <parameter5/>
                    <parameter6/>
                    <parameter7/>
                    <parameter8/>
                    <parameter9/>
                    <parameter10/>
                    <parameter11/>
                </script>
            </scripts>
            <printers>
                <size>0</size>
                <leave_existing_default/>
            </printers>
            <dock_items>
                <size>0</size>
            </dock_items>
            <account_maintenance>
                <accounts>
                    <size>0</size>
                </accounts>
                <directory_bindings>
                    <size>0</size>
                </directory_bindings>
                <management_account>
                    <action>doNotChange</action>
                </management_account>
                <open_firmware_efi_password>
                    <of_mode>none</of_mode>
                    <of_password_sha256/>
                </open_firmware_efi_password>
            </account_maintenance>
            <reboot>
                <message>This computer will restart in 5 minutes. Please save anything you are working on and log out by choosing Log Out from the bottom of the Apple menu.</message>
                <startup_disk>Current Startup Disk</startup_disk>
                <specify_startup/>
                <no_user_logged_in>Do not restart</no_user_logged_in>
                <user_logged_in>Do not restart</user_logged_in>
                <minutes_until_reboot>5</minutes_until_reboot>
                <start_reboot_timer_immediately>false</start_reboot_timer_immediately>
                <file_vault_2_reboot>false</file_vault_2_reboot>
            </reboot>
            <maintenance>
                <recon>false</recon>
                <reset_name>false</reset_name>
                <install_all_cached_packages>false</install_all_cached_packages>
                <heal>false</heal>
                <prebindings>false</prebindings>
                <permissions>false</permissions>
                <byhost>false</byhost>
                <system_cache>false</system_cache>
                <user_cache>false</user_cache>
                <verify>false</verify>
            </maintenance>
            <files_processes>
                <search_by_path/>
                <delete_file>false</delete_file>
                <locate_file/>
                <update_locate_database>false</update_locate_database>
                <spotlight_search/>
                <search_for_process/>
                <kill_process>false</kill_process>
                <run_command/>
            </files_processes>
            <user_interaction>
                <message_start/>
                <allow_users_to_defer>false</allow_users_to_defer>
                <allow_deferral_until_utc/>
                <allow_deferral_minutes>0</allow_deferral_minutes>
                <message_finish/>
            </user_interaction>
            <disk_encryption>
                <action>none</action>
            </disk_encryption>
        </policy>
        """.format(computer_group_id, computer_group_name, script_id, script_name), 0
    )

    # create a policy for printer driver creation
    script_id = classic.get_script(name="printer_driver_creation")['script']['id']
    script_name = classic.get_script(name="printer_driver_creation")['script']['name']

    classic.create_policy(
        """
        <policy>
            <general>
                <name>printer_driver_creation_trial</name>
                <enabled>true</enabled>
                <trigger>USER_INITIATED</trigger>
                <trigger_checkin>false</trigger_checkin>
                <trigger_enrollment_complete>false</trigger_enrollment_complete>
                <trigger_login>false</trigger_login>
                <trigger_network_state_changed>false</trigger_network_state_changed>
                <trigger_startup>true</trigger_startup>
                <trigger_other/>
                <frequency>Ongoing</frequency>
                <retry_event>none</retry_event>
                <retry_attempts>-1</retry_attempts>
                <notify_on_each_failed_retry>false</notify_on_each_failed_retry>
                <location_user_only>false</location_user_only>
                <target_drive>/</target_drive>
                <offline>false</offline>
                <category>
                    <id>104</id>
                    <name>Lifestyle 2023-2024</name>
                </category>
                <date_time_limitations>
                    <activation_date/>
                    <activation_date_epoch>0</activation_date_epoch>
                    <activation_date_utc/>
                    <expiration_date/>
                    <expiration_date_epoch>0</expiration_date_epoch>
                    <expiration_date_utc/>
                    <no_execute_on/>
                    <no_execute_start/>
                    <no_execute_end/>
                </date_time_limitations>
                <network_limitations>
                    <minimum_network_connection>No Minimum</minimum_network_connection>
                    <any_ip_address>true</any_ip_address>
                    <network_segments/>
                </network_limitations>
                <override_default_settings>
                    <target_drive>/</target_drive>
                    <distribution_point>default</distribution_point>
                    <force_afp_smb>false</force_afp_smb>
                    <sus>default</sus>
                </override_default_settings>
                <network_requirements>Any</network_requirements>
                <site>
                    <id>-1</id>
                    <name>None</name>
                </site>
            </general>
            <scope>
                <all_computers>false</all_computers>
                <computers/>
                <computer_groups>
                    <computer_group>
                        <id>{0}</id>
                        <name>{1}</name>
                    </computer_group>
                </computer_groups>
                <buildings/>
                <departments/>
                <limit_to_users>
                    <user_groups/>
                </limit_to_users>
                <limitations>
                    <users/>
                    <user_groups/>
                    <network_segments/>
                    <ibeacons/>
                </limitations>
                <exclusions>
                    <computers/>
                    <computer_groups/>
                    <buildings/>
                    <departments/>
                    <users/>
                    <user_groups/>
                    <network_segments/>
                    <ibeacons/>
                </exclusions>
            </scope>
            <self_service>
                <use_for_self_service>true</use_for_self_service>
                <self_service_display_name>Printer Driver for SW Faculty Staff</self_service_display_name>
                <install_button_text>Install</install_button_text>
                <reinstall_button_text>Reinstall</reinstall_button_text>
                <self_service_description/>
                <force_users_to_view_description>false</force_users_to_view_description>
                <self_service_icon/>
                <feature_on_main_page>false</feature_on_main_page>
                <self_service_categories>
                    <category>
                        <id>94</id>
                        <name>On-Boarding Staff 2023</name>
                        <display_in>true</display_in>
                        <feature_in>false</feature_in>
                    </category>
                    <category>
                        <id>89</id>
                        <name>Printer driver Equitrac V6</name>
                        <display_in>true</display_in>
                        <feature_in>false</feature_in>
                    </category>
                </self_service_categories>
                <notification>false</notification>
                <notification_type>Self Service</notification_type>
                <notification_subject>Trial Version - Fuji Xerox - C4570</notification_subject>
                <notification_message/>
            </self_service>
            <package_configuration>
                <packages>
                    <size>5</size>
                    <package>
                        <id>1066</id>
                        <name>Booklet and Finisher Driver.dmg</name>
                        <action>Install</action>
                        <fut>true</fut>
                        <feu>true</feu>
                    </package>
                    <package>
                        <id>1068</id>
                        <name>FF Printer Driver 2022 Sept 19.dmg</name>
                        <action>Install</action>
                        <fut>true</fut>
                        <feu>true</feu>
                    </package>
                    <package>
                        <id>555</id>
                        <name>Fuji Xerox PS Plug-in Installer.pkg</name>
                        <action>Install</action>
                        <fut>false</fut>
                        <feu>false</feu>
                    </package>
                    <package>
                        <id>1069</id>
                        <name>FUJIFILM PS Plug-in Installer- Main Driver.pkg</name>
                        <action>Install</action>
                        <fut>false</fut>
                        <feu>false</feu>
                    </package>
                    <package>
                        <id>1070</id>
                        <name>printerpreset7070.dmg</name>
                        <action>Install</action>
                        <fut>true</fut>
                        <feu>true</feu>
                    </package>
                </packages>
                <distribution_point>default</distribution_point>
            </package_configuration>
            <scripts>
                <size>3</size>
                <script>
                    <id>441</id>
                    <name>PrinterPreset activate</name>
                    <priority>After</priority>
                    <parameter4/>
                    <parameter5/>
                    <parameter6/>
                    <parameter7/>
                    <parameter8/>
                    <parameter9/>
                    <parameter10/>
                    <parameter11/>
                </script>
                <script>
                    <id>361</id>
                    <name>RemoveHKISPrinters.sh</name>
                    <priority>Before</priority>
                    <parameter4/>
                    <parameter5/>
                    <parameter6/>
                    <parameter7/>
                    <parameter8/>
                    <parameter9/>
                    <parameter10/>
                    <parameter11/>
                </script>
                <script>
                    <id>{2}</id>
                    <name>{3}</name>
                    <priority>After</priority>
                    <parameter4/>
                    <parameter5/>
                    <parameter6/>
                    <parameter7/>
                    <parameter8/>
                    <parameter9/>
                    <parameter10/>
                    <parameter11/>
                </script>
            </scripts>
            <printers>
                <size>0</size>
                <leave_existing_default/>
            </printers>
            <dock_items>
                <size>0</size>
            </dock_items>
            <account_maintenance>
                <accounts>
                    <size>0</size>
                </accounts>
                <directory_bindings>
                    <size>0</size>
                </directory_bindings>
                <management_account>
                    <action>doNotChange</action>
                </management_account>
                <open_firmware_efi_password>
                    <of_mode>none</of_mode>
                    <of_password_sha256/>
                </open_firmware_efi_password>
            </account_maintenance>
            <reboot>
                <message>This computer will restart in 5 minutes. Please save anything you are working on and log out by choosing Log Out from the bottom of the Apple menu.</message>
                <startup_disk>Current Startup Disk</startup_disk>
                <specify_startup/>
                <no_user_logged_in>Do not restart</no_user_logged_in>
                <user_logged_in>Do not restart</user_logged_in>
                <minutes_until_reboot>5</minutes_until_reboot>
                <start_reboot_timer_immediately>false</start_reboot_timer_immediately>
                <file_vault_2_reboot>false</file_vault_2_reboot>
            </reboot>
            <maintenance>
                <recon>true</recon>
                <reset_name>false</reset_name>
                <install_all_cached_packages>false</install_all_cached_packages>
                <heal>false</heal>
                <prebindings>false</prebindings>
                <permissions>false</permissions>
                <byhost>false</byhost>
                <system_cache>false</system_cache>
                <user_cache>false</user_cache>
                <verify>false</verify>
            </maintenance>
            <files_processes>
                <search_by_path/>
                <delete_file>false</delete_file>
                <locate_file/>
                <update_locate_database>false</update_locate_database>
                <spotlight_search/>
                <search_for_process/>
                <kill_process>false</kill_process>
                <run_command/>
            </files_processes>
            <user_interaction>
                <message_start/>
                <allow_users_to_defer>false</allow_users_to_defer>
                <allow_deferral_until_utc/>
                <allow_deferral_minutes>0</allow_deferral_minutes>
                <message_finish/>
            </user_interaction>
            <disk_encryption>
                <action>none</action>
            </disk_encryption>
        </policy>
        """.format(computer_group_id, computer_group_name, script_id, script_name) , 0

    )



    f = input("Press ENTER to continue...")

    with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:

        for i_index, i_value in enumerate(shared.excel_data):

            SerialNumber = i_value[-1]	# *
            try:
                for_the_managemenent_id = classic.get_computer(serialnumber=SerialNumber)['computer']['general']['id']
            except Exception as e:
                print(f"Error retrieving device {SerialNumber}: {e}")
                shared.missing_computers.append(SerialNumber)
                continue

            with Pro(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as pro:
                try:
                    management_id =  pro.get_computer_inventory(for_the_managemenent_id)['general']['managementId']
                    print(management_id)
                except Exception as e:
                    print(f"Error retrieving device {SerialNumber}: {e}")
                    shared.missing_computers.append(SerialNumber)

                # the endpoint actually have a problem. This has to be updated in the pro.py file
                # command click on the pro.create_mdm_command to see the pro.py file
                # change the endpoint to the desired endpoint in this case endpoint = "/api/preview/mdm/commands"
                # save the pro.py file and run the script
                # the json dict for the parameter can be generated in the jamf classic api link
                # simply go to the corresponding api, fill in the parameters, in language click on Python copy the dictionary under payload = ...
                # The management id can be found under the inventory, general, Jamf Pro Management ID: ...

                pro.create_mdm_command(
                    {
                    "commandData": {
                        "commandType": "SETTINGS",
                        "deviceName": f"{full_name_list[i_index]}'s Happiest Mac In THE WORLD",
                    },
                    "clientData": [
                        {
                        "managementId": management_id
                        }
                    ]
                    }
                )



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
    

                pro.create_mdm_command(
                    {
                    "commandData": {
                        "commandType": "RESTART_DEVICE",
                        "rebuildKernelCache": False
                    },
                    "clientData": [
                        {
                        "managementId": management_id
                        }
                    ]
                    }
                )
                continue

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
            
                    






                

            

        