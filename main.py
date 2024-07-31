from my_module import *

JPS_URL = "https://jss.hkis.edu.hk:8443/"
JPS_USERNAME = environ.get("JPS_USERNAME")
JPS_PASSWORD = environ.get("JPS_PASSWORD")

xlsx_file_path = '/Users/lawerance/repo/Book.xlsx'

#Run the script
#Get data from excel
shared.excel_data = getdata.get_data_from_xlsx(xlsx_file_path)

# update_jamf.Execute(JPS_URL, JPS_USERNAME,JPS_PASSWORD)

reset_computer.reset(JPS_URL, JPS_USERNAME,JPS_PASSWORD)





