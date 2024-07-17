from my_module import *

def get_data_from_xlsx(file_path):
    data_list = []
    df = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=1, usecols='A:B')
    for index, row in df.iterrows():
        data_list.append(row.tolist())
    return data_list

# Example usage
xlsx_file_path = '/Users/lawerance/repo/Book.xlsx'
data = get_data_from_xlsx(xlsx_file_path)
print(data)
