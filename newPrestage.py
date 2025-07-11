# deprecated
# this is to be put 
from my_module import *


def pre_enroll(JPS_URL, JPS_USERNAME,JPS_PASSWORD):
    with Pro(JPS_URL, JPS_USERNAME,JPS_PASSWORD) as pro:
        try:
            # x = pro.get_computer_prestage(id=16)
            # with open("output.txt", "w") as f:
            #     f.write(str(x))
            #     exit()
            pro.delete_computer_prestage(id=100) 
            # the delete has to be put at the end of the whole thing like really the whole thing since the prestage would need to apply for the computer setup. 

        except Exception as e:  
            print(f"Error creating prestage: {e}")
        pro.create_computer_prestage(
        {
            'keepExistingSiteMembership': False, 'enrollmentSiteId': '-1', 'displayName': 'Enrollment_trial_v5', 'supportPhoneNumber': '', 'supportEmailAddress': 'elaw', 'department': '', 'mandatory': True, 'mdmRemovable': True, 'defaultPrestage': False, 'keepExistingLocationInformation': False, 'requireAuthentication': False, 'authenticationPrompt': '', 'profileUuid': '407FC0021A503B910FA020612857D6D2', 'deviceEnrollmentProgramInstanceId': '1', 'versionLock': 2, 'siteId': '-1', 'skipSetupItems': {'Biometric': True, 'TermsOfAddress': False, 'FileVault': False, 'iCloudDiagnostics': True, 'Diagnostics': True, 'Accessibility': True, 'AppleID': True, 'ScreenTime': True, 'Siri': True, 'DisplayTone': True, 'Restore': True, 'Appearance': True, 'Privacy': True, 'Payment': True, 'Registration': True, 'TOS': True, 'iCloudStorage': True, 'Location': False}, 'locationInformation': {'username': 'elaw', 'realname': '', 'phone': '', 'email': '', 'room': '', 'position': '', 'departmentId': '-1', 'buildingId': '-1', 'id': '114', 'versionLock': 1}, 'purchasingInformation': {'id': '12', 'leased': False, 'purchased': True, 'appleCareId': '', 'poNumber': '', 'vendor': '', 'purchasePrice': '', 'lifeExpectancy': 0, 'purchasingAccount': '', 'purchasingContact': '', 'leaseDate': '1970-01-01', 'poDate': '1970-01-01', 'warrantyDate': '1970-01-01', 'versionLock': 0}, 'preventActivationLock': False, 'enableDeviceBasedActivationLock': False, 'anchorCertificates': [], 'enrollmentCustomizationId': '100', 'language': '', 'region': '', 'autoAdvanceSetup': False, 'customPackageIds': [], 'customPackageDistributionPointId': '-1', 'installProfilesDuringSetup': False, 'prestageInstalledProfileIds': [], 'enableRecoveryLock': False, 'recoveryLockPasswordType': 'MANUAL', 'rotateRecoveryLockPassword': False, 'accountSettings': {'id': '16', 'payloadConfigured': True, 'localAdminAccountEnabled': True, 'adminUsername': 'useradmin', 'hiddenAdminAccount': False, 'localUserManaged': False, 'userAccountType': 'ADMINISTRATOR', 'versionLock': 1, 'prefillPrimaryAccountInfoFeatureEnabled': False, 'prefillType': 'CUSTOM', 'prefillAccountFullName': '', 'prefillAccountUserName': '', 'preventPrefillInfoFromModification': False}
        }            
        )

        # Create the PreStage
        create_url = f"{JAMF_URL}/api/v2/computer-prestages"
        response = requests.post(create_url, headers=headers, json=prestage_payload)
        prestage_data = response.json()

        # Capture the PreStage ID for later deletion
        PRESTAGE_ID = prestage_data["id"]
        print(f"Created PreStage ID: {PRESTAGE_ID}")


        
        print("Prestage created")
            

        
    
    
# tbc
from my_module import *

def pre_enroll(JPS_URL, JPS_USERNAME, JPS_PASSWORD):
    # Initialize prestage_id as None to track creation status
    prestage_id = None
    
    try:
        with Pro(JPS_URL, JPS_USERNAME, JPS_PASSWORD) as pro:
            # Create the prestage and capture its ID
            prestage_response = pro.create_computer_prestage({
                'keepExistingSiteMembership': False,
                'enrollmentSiteId': '-1',
                'displayName': 'Enrollment_trial_v5',
                # ... (rest of your prestage payload) ...
            })
            
            # Extract the ID from the response
            prestage_id = prestage_response['id']  # Adjust this if response structure differs
            print(f"Temporary PreStage created with ID: {prestage_id}")
            
            # ----------------------------------
            # YOUR MAIN OPERATIONS GO HERE
            # All code that needs the PreStage to exist
            # ----------------------------------
            
    except Exception as e:
        print(f"Error during operations: {e}")
        raise  # Re-raise if you want calling code to handle
        
    finally:
        # This block runs whether try succeeds or fails
        if prestage_id is not None:
            try:
                with Pro(JPS_URL, JPS_USERNAME, JPS_PASSWORD) as pro:
                    pro.delete_computer_prestage(id=prestage_id)
                    print(f"Successfully cleaned up PreStage {prestage_id}")
            except Exception as cleanup_error:
                print(f"Failed to cleanup PreStage {prestage_id}: {cleanup_error}")