# PythonJamfHKIS

This is a new project using JAMF Pro incooporating with Python using API to monitor and manipulate MACs.

Install the following applications
Assume installed: Python3, VS Code is recommended. In VS Code install extensions GitHub Desktop, Git Extension Pack

For jps-api-wrapper 
- pip3 install jps-api-wrapper 
For xml files            
- pip3 install lxml
For pandas                 
- pip3 install pandas       
For xlsx files        
- pip3 install openpyxl              
Install the repo from Github with the URL

For mac, type the following in terminal
setopt HIST_IGNORE_SPACE
export JPS_USERNAME=yourUsername
export JPS_PASSWORD=yourPassword

For Windows, type the following in terminal
set JPS_USERNAME=yourUsername
set JPS_PASSWORD=yourPassword

Fill in the .xlsx file from the web.
Download the .xlsx file from the web. Use pwd in terminal to get the path of the file.
Specify the path in main.py.                                    xlsx_file_path = the_path
Change the endpoint in the pro.py file                          endpoint = "/api/preview/mdm/commands"


Run the main.py and you are good to go.

# Remarks
- When executing reset_computer.py
        For a local user account to be created on the specified mac.
        In Jamf Pro, open seetings type script to located the script uploaded by the reset_computer.py.
        Create a policy under computer, under policies.
        Specify the Name, and under trigger select Startup, Login and enrollment complete. Under Execution Frequency select Once per computer.
        Under the scripts, click + located on the top right hand corner.
        Find the name of the script and add. (By cmd + f)
        In the scope, under target computer select a computer group or a specific computer.
        Under selected Deployment targets add the computer group or sepcific computer you want.
        Click Save on the bottom right hand corner.

        On the spcified computer,
        Open terminal.
        Type sudo jamf recon
        And in the console, under the Log Report tab, find the jamf.log file to see what is going on.

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
        # simply go to the corresponding api, fill in the parameters, in language click on Python copy the dictionary under payload = ...
        # The management id can be found under the inventory, general, Jamf Pro Management ID: ...
- Beware of endpoint deprecation. This means that the API developers have marked it as outdated and no longer recommend using it for new applications or integrations. This is often done when a newer, better, or more efficient endpoint replaces the deprecated one.
        # This can be found in the jamf classic api link. Marked with a ! next to the corresponding api.
        # It is also marked indise the pro.py library e.g.                 
        "Pro.create_macos_managed_software_updates has been deprecated by Jamf "
                "Pro v10.44.0."
- A Mac maybe unmanaged on Jamf.
        use sudo profiles renew -type enrollment        on the corresponding mac in terminal to manage the mac on JAMF.





# References
- https://community.jamf.com/t5/tech-thoughts/introduction-to-jps-api-wrapper-all-in-one-package-for-using-the/ba-p/283126
- https://gitlab.com/cvtc/appleatcvtc/jps-api-wrapper/-/blob/main/README.md#retrieving-the-password-in-python-and-authenticating
- https://jps-api-wrapper.readthedocs.io/en/stable/
- https://developer.jamf.com/jamf-pro/reference/classic-api
- https://jss.hkis.edu.hk:8443/api/doc/#/mdm/get_v1_mdm_commands     # This is swagger UI
- https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10 # This is error message for reference
- https://www.jamf.com/blog/howto-erase-all-content-and-settings-macos-redeployment/ #reference for erase device
- https://community.jamf.com/t5/tech-thoughts/how-to-securely-manage-local-admin-passwords-with-jamf-pro-and/ba-p/289969 # for management id
- https://community.jamf.com/t5/jamf-pro/computer-showing-in-jamf-as-unmanaged/m-p/291741 #for jamf re enrollment

* Return to service articles
- https://www.youtube.com/watch?v=PyYp0pfxWCw # Youtube Guide
- https://www.youtube.com/watch?v=uZcN3d4HSUk # Youtube Demo
- https://support.apple.com/en-gb/guide/deployment/dep0a819891e/web # Return to service
- https://learn.jamf.com/en-US/bundle/technical-articles/page/Return_to_Service.html # Return to service
- https://s3.us-west-2.amazonaws.com/jamfse.io/Jamf+Return+to+Service+-+Guide.pdf # Retuen to service
- https://www.youtube.com/watch?v=6M_1ruG6Pys   # Automated Device Enrollment
- https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Automated_Device_Enrollment_Integration.html#:~:text=In%20Jamf%20Pro%2C%20click%20Settings,section%2C%20click%20Automated%20Device%20Enrollment%20. #Automated Device Enrollment
- https://api-docs.kandji.io/#149ae2cc-fb7f-42ce-8379-187878685303 # return to service does not work on macos

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




