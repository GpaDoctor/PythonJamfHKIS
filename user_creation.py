# deprecated
from my_module import *

# def create_user(username, password, full_name):
#     try:
#         # Create the user
#         subprocess.run(['sudo', 'dscl', '.', '-create', f'/Users/{username}'], check=True)
#         subprocess.run(['sudo', 'dscl', '.', '-create', f'/Users/{username}', 'UserShell', '/bin/bash'], check=True)
#         subprocess.run(['sudo', 'dscl', '.', '-create', f'/Users/{username}', 'RealName', full_name], check=True)
#         subprocess.run(['sudo', 'dscl', '.', '-create', f'/Users/{username}', 'UniqueID', '510'], check=True)
#         subprocess.run(['sudo', 'dscl', '.', '-create', f'/Users/{username}', 'PrimaryGroupID', '20'], check=True)
#         subprocess.run(['sudo', 'dscl', '.', '-create', f'/Users/{username}', 'NFSHomeDirectory', f'/Users/{username}'], check=True)
#         subprocess.run(['sudo', 'dscl', '.', '-passwd', f'/Users/{username}', password], check=True)
       
#         # Add the user to the admin group
#         subprocess.run(['sudo', 'dscl', '.', '-append', '/Groups/admin', 'GroupMembership', username], check=True)
       
#         print(f"User {username} created successfully.")
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred: {e}")



class JamfManager:
    def __init__(self, jamf_url, username, password):
        self.jamf_url = jamf_url
        self.username = username
        self.password = password
        self.token = self.get_auth_token()

    def get_auth_token(self):
        url = f'{self.jamf_url}/api/v1/auth/token'
        response = requests.post(url, auth=(self.username, self.password))
        response.raise_for_status()
        return response.json()['token']

    # def find_mac_by_serial(self, serial_number):
    #     url = f'{self.jamf_url}/JSSResource/computers/serialnumber/{serial_number}'
    #     headers = {'Authorization': f'Bearer {self.token}'}
    #     response = requests.get(url, headers=headers)
    #     response.raise_for_status()
    #     return response.json()

    def create_local_user(self, computer_id, new_username, new_password, full_name):
        # mac_info = self.find_mac_by_serial(serial_number)
        # computer_id = mac_info['computer']['general']['id']

        url = f'{self.jamf_url}/JSSResource/computercommands/command/CreateAccount'
        headers = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json'}
        payload = {
            "computer_id": computer_id,
            "username": new_username,
            "realname": full_name,
            "password": new_password,
            "home": f"/Users/{new_username}",
            "admin": True
        }

        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        print(f"User {new_username} created successfully on Mac with serial number {computer_id}.")
