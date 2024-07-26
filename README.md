# PythonJamfHKIS

This is a new project using JEMF incooporating with Python using API to monitor and manipulate MACs.

Install the following applications
Assume installed: Python3, git, VS Code is recommended
- pip3 install jps-api-wrapper       jps-api-wrapper       
- pip3 install lxml                  for xml files
- pip3 install pandas                for csv files
- pip3 install openpyxl               for xlsx files

For mac, type the following in terminal
setopt HIST_IGNORE_SPACE
export JPS_USERNAME=yourUsername
export JPS_PASSWORD=yourPassword

For Windows, type the following in terminal
set JPS_USERNAME=yourUsername
set JPS_PASSWORD=yourPassword

specify the path in getdata.py

run the main.py and you are good to go

*Remarks
- INCASE unable to refresh authentication. Restart VS Code completely and retype the authentication.
- INCASE import does not work. Click the bottom right hand corner Python 3.12.4 64-bit. Choose Global, then choose back Recommened.
- Beware of Captitalization. Especially in  with Pro(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as pro: and with Classic(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as classic:
- Beware when using pro.py when a 405 error shows up
        #For example: in the pro.create_mdm_command
        # the endpoint actually have a problem. This has to be updated in the pro.py file
        # command click on the pro.create_mdm_command to see the pro.py file
        # change the endpoint to the desired endpoint in this case endpoint = "/api/preview/mdm/commands"
        # save the pro.py file and run the script
        # the json dict for the parameter can be generated in the jamf classic api link
        #simply go to the corresponding api, fill in the parameters, in language click on Python copy the dictionary under payload = ...
        # The management id can be found under the inventory, general, Jamf Pro Management ID: ...
- Beware of endpoint deprecation. This means that the API developers have marked it as outdated and no longer recommend using it for new applications or integrations. This is often done when a newer, better, or more efficient endpoint replaces the deprecated one.
        # This can be found in the jamf classic api link. Marked with a ! next to the corresponding api.
        # It is also marked indise the pro.py library e.g.                 
        "Pro.create_macos_managed_software_updates has been deprecated by Jamf "
                "Pro v10.44.0."




source:
- https://community.jamf.com/t5/tech-thoughts/introduction-to-jps-api-wrapper-all-in-one-package-for-using-the/ba-p/283126
- https://gitlab.com/cvtc/appleatcvtc/jps-api-wrapper/-/blob/main/README.md#retrieving-the-password-in-python-and-authenticating
- https://jps-api-wrapper.readthedocs.io/en/stable/
- https://developer.jamf.com/jamf-pro/reference/classic-api
- https://jss.hkis.edu.hk:8443/api/doc/#/mdm/get_v1_mdm_commands     # This is swagger UI
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10 # This is error message for reference
- https://www.jamf.com/blog/howto-erase-all-content-and-settings-macos-redeployment/ #reference for erase device
- https://community.jamf.com/t5/tech-thoughts/how-to-securely-manage-local-admin-passwords-with-jamf-pro-and/ba-p/289969 # for management id

# Return to service articles
- https://www.youtube.com/watch?v=PyYp0pfxWCw # Youtube Guide
- https://support.apple.com/en-gb/guide/deployment/dep0a819891e/web # Return to service
- https://learn.jamf.com/en-US/bundle/technical-articles/page/Return_to_Service.html # Return to service
- https://www.youtube.com/watch?v=6M_1ruG6Pys   # Automated Device Enrollment
- https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Automated_Device_Enrollment_Integration.html#:~:text=In%20Jamf%20Pro%2C%20click%20Settings,section%2C%20click%20Automated%20Device%20Enrollment%20. #Automated Device Enrollment

Steps:
1. Need to create a configuration profile in Jamf Pro
2. Under COMPUTER, under Configuration Profile
3. Click New
4. In General, name it as return_to_service_wifi
5. Under WIFI, type in the SSID aka the name of the WIFI
6. Download the profile
7. https://community.jamf.com/t5/jamf-pro/viewing-editing-casper-mobileconfig-files/m-p/35588       # Turn mobile.config to an xml readable format

security cms -D -i return_to_service_wifi.mobileconfig | xmllint --pretty 1 - > return_to_service_wifi.xml

8. https://www.base64encode.org/ # base64 encoding




