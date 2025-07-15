# import requests
# response = requests.get("https://jss.hkis.edu.hk:8443/api/endpoint")  # No `verify=False` needed!
# print(response.status_code)




# #!/bin/bash

# # Check if Location Services is already enabled
# if [[ $(/usr/bin/defaults read /var/db/locationd/Library/Preferences/ByHost/com.apple.locationd.plist LocationServicesEnabled) == "1" ]]; then
#   echo "Location Services already enabled"
#   exit 0
# fi

# # Enable Location Services
# /usr/bin/defaults write /var/db/locationd/Library/Preferences/ByHost/com.apple.locationd.plist LocationServicesEnabled -int 1
# /bin/launchctl kickstart -k system/com.apple.locationd

# echo "Location Services enabled"
# exit 0





from my_module import *

def test(JPS_URL, JPS_USERNAME, JPS_PASSWORD):
    # Connect to Jamf
    with Classic(JPS_URL, JPS_USERNAME, JPS_PASSWORD) as classic:
        # Get computer details
        computer_info = classic.get_computer(serialnumber="FVFFL2BKQ6LT")
        computer_id = computer_info["computer"]["general"]["id"]
        print("Computer ID:", computer_id)

        with Pro(JPS_URL, JPS_USERNAME, JPS_PASSWORD) as pro:
            # Pass the actual ID variable, not a string
            computer = pro.get_computer_inventory(id=str(computer_id))  # Convert to string if needed
            print("Last enrolled:", computer['general']['lastEnrolledDate'])