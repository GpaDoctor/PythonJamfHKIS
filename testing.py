# import requests
# response = requests.get("https://jss.hkis.edu.hk:8443/api/endpoint")  # No `verify=False` needed!
# print(response.status_code)



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