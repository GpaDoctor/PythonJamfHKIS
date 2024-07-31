from my_module import *

def get_data_from_xlsx(file_path):
    data_list = []                                              
    df = pd.read_excel(file_path, sheet_name='Sheet1', usecols='A,B,E,F,K,L,N,P,Q,U', skiprows=1,header=None)
    for index, row in df.iterrows():
        data_list.append(row.tolist())
        
    return data_list

# if __name__ == "__main__": #    checks if the script is being run directly (i.e., not being imported). If true, it executes the block of code indented under it. This is useful for running script-specific code (like tests or example usage) only when the script is executed directly, and not when it's imported as a module in another script.
#     # Example usage
#     xlsx_file_path = '/Users/lawerance/repo/Book.xlsx'
#     data = get_data_from_xlsx(xlsx_file_path)
#     # print(data)

#     for i in data:
#         print(i)