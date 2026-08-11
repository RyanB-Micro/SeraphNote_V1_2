from Sheet import Sheet

class Project:
    def __init__(self):
        self.name = "SeraphNote__New_File__.pk1"
        self.description = "New Seraph Project"
        self.author = ""
        self.sheet_count = 0
        self.active_sheet_indx = None
        self.project_sheets = []

    def create_sheet(self, sheet_name):
        new_sheet = Sheet(sheet_name)
        self.project_sheets.append(new_sheet)
        self.sheet_count += 1

    def delete_sheet(self, sheet_name):
        # search for sheet to remove
        for sheet in self.project_sheets:
            if sheet.sheet_name == sheet_name:
                self.project_sheets.remove(sheet)
                self.sheet_count -= 1