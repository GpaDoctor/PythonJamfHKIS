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
        #             "deviceId": "9564"
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
                    "commandType": "ERASE_DEVICE",
                    "disallowProximitySetup": True,
                    "pin": "123456"
                },
                "clientData": [{ "managementId": " 4d7203c7-6043-4dae-8341-265768a15e5f" }]
            }
        )

