from my_module import *

def main():
    JPS_URL = "https://jss.hkis.edu.hk:8443/"
    JPS_USERNAME = environ.get("JPS_USERNAME")
    JPS_PASSWORD = environ.get("JPS_PASSWORD")

    if not JPS_USERNAME or not JPS_PASSWORD:
        raise ValueError("JPS_USERNAME and JPS_PASSWORD must be set in the environment variables.")

    xlsx_file_path = '/Users/jamf/Documents/repo/Book.xlsx'

    #Run the script
    # Get data from excel
    shared.excel_data = getdata.get_data_from_xlsx(xlsx_file_path)


    reset_computer.reset(JPS_URL, JPS_USERNAME, JPS_PASSWORD)

    time.sleep(5)

    update_jamf.Execute(JPS_URL, JPS_USERNAME, JPS_PASSWORD)



  

    # prestage.pre_enroll(JPS_URL, JPS_USERNAME, JPS_PASSWORD)


    

if __name__ == "__main__":
    main()





