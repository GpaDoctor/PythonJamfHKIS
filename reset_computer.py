from my_module import *

def reset(JPS_URL, JPS_USERNAME,JPS_PASSWORD):
	# Connect to Jemf

    with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:

        SerialNumber = "C02YV2LAJK7M"	# *
        try:
            DeviceNeedUpdating = classic.get_computer(serialnumber=SerialNumber)
        except Exception as e:
            print(f"Error retrieving device {SerialNumber}: {e}")
            shared.missing_computers.append(SerialNumber)
            # continue

    with Pro(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as pro:
        pro.create_mdm_command(
            """
            {
            "commandData": {
                "commandType": "LOG_OUT_USER"
            },
            "clientData": [
                {
                "managementId": "aaaaaaaa-3f1e-4b3a-a5b3-ca0cd7430937"
                }
            ]
            }
            """
        )