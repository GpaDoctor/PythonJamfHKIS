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

        # pro.create_mdm_command(
        #     {
        #         "commandData": {
        #             "commandType": "ERASE_DEVICE",
        #             "disallowProximitySetup": True,
        #             "pin": "123456"
        #         },
        #         "clientData": [{ "managementId": " 4d7203c7-6043-4dae-8341-265768a15e5f" }]
        #     }
        # )



#         pro.create_return_to_service_configuration(
# {
#     "displayName": "false",
#     "wifiProfileId": "65&o=r"
# }

#         )



        pro.create_mdm_command(
            {
                "commandData": {
                    "commandType": "ERASE_DEVICE",
                    "returnToService": {
                        "enabled": True,
                        "mdmProfileData": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHBsaXN0IFBVQkxJQyAiLS8vQXBwbGUvL0RURCBQTElTVCAxLjAvL0VOIiAiaHR0cDovL3d3dy5hcHBsZS5jb20vRFREcy9Qcm9wZXJ0eUxpc3QtMS4wLmR0ZCI+CjxwbGlzdCB2ZXJzaW9uPSIxIj4KICA8ZGljdD4KICAgIDxrZXk+UGF5bG9hZFVVSUQ8L2tleT4KICAgIDxzdHJpbmc+ODg3RDA4QzgtNDk0MS00OUNBLUJDNkEtNUMzMDYxQkYzNUU3PC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWRUeXBlPC9rZXk+CiAgICA8c3RyaW5nPkNvbmZpZ3VyYXRpb248L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZE9yZ2FuaXphdGlvbjwva2V5PgogICAgPHN0cmluZz5Ib25nIEtvbmcgSW50ZXJuYXRpb25hbCBTY2hvb2w8L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZElkZW50aWZpZXI8L2tleT4KICAgIDxzdHJpbmc+ODg3RDA4QzgtNDk0MS00OUNBLUJDNkEtNUMzMDYxQkYzNUU3PC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWREaXNwbGF5TmFtZTwva2V5PgogICAgPHN0cmluZz5yZXR1cm5fdG9fc2VydmljZV93aWZpPC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWREZXNjcmlwdGlvbjwva2V5PgogICAgPHN0cmluZy8+CiAgICA8a2V5PlBheWxvYWRWZXJzaW9uPC9rZXk+CiAgICA8aW50ZWdlcj4xPC9pbnRlZ2VyPgogICAgPGtleT5QYXlsb2FkRW5hYmxlZDwva2V5PgogICAgPHRydWUvPgogICAgPGtleT5QYXlsb2FkUmVtb3ZhbERpc2FsbG93ZWQ8L2tleT4KICAgIDx0cnVlLz4KICAgIDxrZXk+UGF5bG9hZFNjb3BlPC9rZXk+CiAgICA8c3RyaW5nPlN5c3RlbTwvc3RyaW5nPgogICAgPGtleT5QYXlsb2FkQ29udGVudDwva2V5PgogICAgPGFycmF5PgogICAgICA8ZGljdD4KICAgICAgICA8a2V5PlBheWxvYWRVVUlEPC9rZXk+CiAgICAgICAgPHN0cmluZz5EOUI3MTc5NC0xNzMyLTRENzQtQUFDNS1BMjgxNTQ2OEUwNzI8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWRUeXBlPC9rZXk+CiAgICAgICAgPHN0cmluZz5jb20uYXBwbGUud2lmaS5tYW5hZ2VkPC9zdHJpbmc+CiAgICAgICAgPGtleT5QYXlsb2FkT3JnYW5pemF0aW9uPC9rZXk+CiAgICAgICAgPHN0cmluZz5Ib25nIEtvbmcgSW50ZXJuYXRpb25hbCBTY2hvb2w8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWRJZGVudGlmaWVyPC9rZXk+CiAgICAgICAgPHN0cmluZz5EOUI3MTc5NC0xNzMyLTRENzQtQUFDNS1BMjgxNTQ2OEUwNzI8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWREaXNwbGF5TmFtZTwva2V5PgogICAgICAgIDxzdHJpbmc+V2lGaSAoQXBwbGUgTmV0d29yayAxY2IzMGYgNUdIeik8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWREZXNjcmlwdGlvbjwva2V5PgogICAgICAgIDxzdHJpbmcvPgogICAgICAgIDxrZXk+UGF5bG9hZFZlcnNpb248L2tleT4KICAgICAgICA8aW50ZWdlcj4xPC9pbnRlZ2VyPgogICAgICAgIDxrZXk+UGF5bG9hZEVuYWJsZWQ8L2tleT4KICAgICAgICA8dHJ1ZS8+CiAgICAgICAgPGtleT5ISURERU5fTkVUV09SSzwva2V5PgogICAgICAgIDxmYWxzZS8+CiAgICAgICAgPGtleT5QYXNzd29yZDwva2V5PgogICAgICAgIDxzdHJpbmc+YTEyMzQ1Njc4PC9zdHJpbmc+CiAgICAgICAgPGtleT5FbmNyeXB0aW9uVHlwZTwva2V5PgogICAgICAgIDxzdHJpbmc+V1BBMzwvc3RyaW5nPgogICAgICAgIDxrZXk+QXV0b0pvaW48L2tleT4KICAgICAgICA8dHJ1ZS8+CiAgICAgICAgPGtleT5DYXB0aXZlQnlwYXNzPC9rZXk+CiAgICAgICAgPGZhbHNlLz4KICAgICAgICA8a2V5PlByb3h5VHlwZTwva2V5PgogICAgICAgIDxzdHJpbmc+Tm9uZTwvc3RyaW5nPgogICAgICAgIDxrZXk+U2V0dXBNb2Rlczwva2V5PgogICAgICAgIDxhcnJheS8+CiAgICAgICAgPGtleT5TU0lEX1NUUjwva2V5PgogICAgICAgIDxzdHJpbmc+QXBwbGUgTmV0d29yayAxY2IzMGYgNUdIejwvc3RyaW5nPgogICAgICAgIDxrZXk+SW50ZXJmYWNlPC9rZXk+CiAgICAgICAgPHN0cmluZz5CdWlsdEluV2lyZWxlc3M8L3N0cmluZz4KICAgICAgPC9kaWN0PgogICAgPC9hcnJheT4KICA8L2RpY3Q+CjwvcGxpc3Q+Cg==",
                        "wifiProfileData": "PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPCFET0NUWVBFIHBsaXN0IFBVQkxJQyAiLS8vQXBwbGUvL0RURCBQTElTVCAxLjAvL0VOIiAiaHR0cDovL3d3dy5hcHBsZS5jb20vRFREcy9Qcm9wZXJ0eUxpc3QtMS4wLmR0ZCI+CjxwbGlzdCB2ZXJzaW9uPSIxIj4KICA8ZGljdD4KICAgIDxrZXk+UGF5bG9hZFVVSUQ8L2tleT4KICAgIDxzdHJpbmc+ODg3RDA4QzgtNDk0MS00OUNBLUJDNkEtNUMzMDYxQkYzNUU3PC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWRUeXBlPC9rZXk+CiAgICA8c3RyaW5nPkNvbmZpZ3VyYXRpb248L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZE9yZ2FuaXphdGlvbjwva2V5PgogICAgPHN0cmluZz5Ib25nIEtvbmcgSW50ZXJuYXRpb25hbCBTY2hvb2w8L3N0cmluZz4KICAgIDxrZXk+UGF5bG9hZElkZW50aWZpZXI8L2tleT4KICAgIDxzdHJpbmc+ODg3RDA4QzgtNDk0MS00OUNBLUJDNkEtNUMzMDYxQkYzNUU3PC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWREaXNwbGF5TmFtZTwva2V5PgogICAgPHN0cmluZz5yZXR1cm5fdG9fc2VydmljZV93aWZpPC9zdHJpbmc+CiAgICA8a2V5PlBheWxvYWREZXNjcmlwdGlvbjwva2V5PgogICAgPHN0cmluZy8+CiAgICA8a2V5PlBheWxvYWRWZXJzaW9uPC9rZXk+CiAgICA8aW50ZWdlcj4xPC9pbnRlZ2VyPgogICAgPGtleT5QYXlsb2FkRW5hYmxlZDwva2V5PgogICAgPHRydWUvPgogICAgPGtleT5QYXlsb2FkUmVtb3ZhbERpc2FsbG93ZWQ8L2tleT4KICAgIDx0cnVlLz4KICAgIDxrZXk+UGF5bG9hZFNjb3BlPC9rZXk+CiAgICA8c3RyaW5nPlN5c3RlbTwvc3RyaW5nPgogICAgPGtleT5QYXlsb2FkQ29udGVudDwva2V5PgogICAgPGFycmF5PgogICAgICA8ZGljdD4KICAgICAgICA8a2V5PlBheWxvYWRVVUlEPC9rZXk+CiAgICAgICAgPHN0cmluZz5EOUI3MTc5NC0xNzMyLTRENzQtQUFDNS1BMjgxNTQ2OEUwNzI8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWRUeXBlPC9rZXk+CiAgICAgICAgPHN0cmluZz5jb20uYXBwbGUud2lmaS5tYW5hZ2VkPC9zdHJpbmc+CiAgICAgICAgPGtleT5QYXlsb2FkT3JnYW5pemF0aW9uPC9rZXk+CiAgICAgICAgPHN0cmluZz5Ib25nIEtvbmcgSW50ZXJuYXRpb25hbCBTY2hvb2w8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWRJZGVudGlmaWVyPC9rZXk+CiAgICAgICAgPHN0cmluZz5EOUI3MTc5NC0xNzMyLTRENzQtQUFDNS1BMjgxNTQ2OEUwNzI8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWREaXNwbGF5TmFtZTwva2V5PgogICAgICAgIDxzdHJpbmc+V2lGaSAoQXBwbGUgTmV0d29yayAxY2IzMGYgNUdIeik8L3N0cmluZz4KICAgICAgICA8a2V5PlBheWxvYWREZXNjcmlwdGlvbjwva2V5PgogICAgICAgIDxzdHJpbmcvPgogICAgICAgIDxrZXk+UGF5bG9hZFZlcnNpb248L2tleT4KICAgICAgICA8aW50ZWdlcj4xPC9pbnRlZ2VyPgogICAgICAgIDxrZXk+UGF5bG9hZEVuYWJsZWQ8L2tleT4KICAgICAgICA8dHJ1ZS8+CiAgICAgICAgPGtleT5ISURERU5fTkVUV09SSzwva2V5PgogICAgICAgIDxmYWxzZS8+CiAgICAgICAgPGtleT5QYXNzd29yZDwva2V5PgogICAgICAgIDxzdHJpbmc+YTEyMzQ1Njc4PC9zdHJpbmc+CiAgICAgICAgPGtleT5FbmNyeXB0aW9uVHlwZTwva2V5PgogICAgICAgIDxzdHJpbmc+V1BBMzwvc3RyaW5nPgogICAgICAgIDxrZXk+QXV0b0pvaW48L2tleT4KICAgICAgICA8dHJ1ZS8+CiAgICAgICAgPGtleT5DYXB0aXZlQnlwYXNzPC9rZXk+CiAgICAgICAgPGZhbHNlLz4KICAgICAgICA8a2V5PlByb3h5VHlwZTwva2V5PgogICAgICAgIDxzdHJpbmc+Tm9uZTwvc3RyaW5nPgogICAgICAgIDxrZXk+U2V0dXBNb2Rlczwva2V5PgogICAgICAgIDxhcnJheS8+CiAgICAgICAgPGtleT5TU0lEX1NUUjwva2V5PgogICAgICAgIDxzdHJpbmc+QXBwbGUgTmV0d29yayAxY2IzMGYgNUdIejwvc3RyaW5nPgogICAgICAgIDxrZXk+SW50ZXJmYWNlPC9rZXk+CiAgICAgICAgPHN0cmluZz5CdWlsdEluV2lyZWxlc3M8L3N0cmluZz4KICAgICAgPC9kaWN0PgogICAgPC9hcnJheT4KICA8L2RpY3Q+CjwvcGxpc3Q+Cg=="
                    },
                    "pin": "123456"
                },
                "clientData": [{ "managementId": " 4d7203c7-6043-4dae-8341-265768a15e5f" }]
            }
        )

