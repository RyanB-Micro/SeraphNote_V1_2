
import pandas as pd
import os

pandas_version = pd.__version__

from Sheet import Sheet

def sheets_to_dataframe(project):
    sheet_data = []
    for sheet in project.project_sheets:
        sheet_data.append(sheet.data_out())

    return pd.DataFrame(sheet_data)


def dataframe_to_sheets(project, sheets_data):
    sheets_list_buffer= []
    for _, row in sheets_data.iterrows():
        new_sheet = Sheet("New_Sheet")
        new_sheet.data_in(row)
        sheets_list_buffer.append(new_sheet)

    return sheets_list_buffer




def save_project(project, filename="SeraphNote_Save_New.pk1"):
    # Create save directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    project_data = {
        'sheets': sheets_to_dataframe(project)
    }

    # Create and save pickle file
    pd.to_pickle(project_data, filename)
    print(f"Project _{filename}_ Saved")



def load_project(project, filename="SeraphNote_Save_New.pk1"):
    load_data = pd.read_pickle(filename)

    sheets_list_buffer = dataframe_to_sheets(project, load_data['sheets'])

    # Replace project sheet list
    project.project_sheets = sheets_list_buffer
