
import pandas as pd
import os

pandas_version = pd.__version__


def save_sheets(project):
    sheet_data = []
    for sheet in project.project_sheets:
        sheet_data.append(sheet.data_out())

    return pd.DataFrame(sheet_data)


def load_sheets():
    pass

def save_project(project, filename="SeraphNote_Save_New.pk1"):
    # Create save directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    project_data = {
        'sheets': project.project_sheets
    }

    # Create and save pickle file
    pd.to_pickle(project_data, filename)
    print(f"Project _{filename}_ Saved")

def load_project(filename="SeraphNote_Save_New.pk1"):
    data_in = pd.read_pickle(filename)
