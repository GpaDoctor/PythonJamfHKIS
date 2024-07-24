from my_module import *

def reset(JPS_URL, JPS_USERNAME,JPS_PASSWORD):
	# Connect to Jemf

    # with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:

    #     SerialNumber = "C02YV2LAJK7M"	# *
    #     try:
    #         classic.get_computer(serialnumber=SerialNumber)
    #     except Exception as e:
    #         print(f"Error retrieving device {SerialNumber}: {e}")
    #         shared.missing_computers.append(SerialNumber)
    #         # continue

    with Pro(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as pro:
        # the endpoint actually have a problem. This has to be updated in the pro.py file
        # command click on the pro.create_mdm_command to see the pro.py file
        # change the endpoint to the desired endpoint in this case endpoint = "/api/preview/mdm/commands"
        # save the pro.py file and run the script
        # The management id can be found under the inventory, general, Jamf Pro Management ID: ...

        pro.create_mdm_command(
            {
            "commandData": {
                "commandType": "SETTINGS",
                "deviceName": "hihi"
            },
            "clientData": [
                {
                "managementId": "4d7203c7-6043-4dae-8341-265768a15e5f"
                }
            ]
            }
        )

