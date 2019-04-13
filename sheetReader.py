import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re


class CharacterSheet:
    """The CharacterSheets will provide a link between the google sheets and the bot"""
    def __init__(self, name):
        scope = ['https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name('driveInformation/client_secret.json', scope)
        client = gspread.authorize(credentials)

        self.name = name
        self.sheet = client.open(self.getSheetName()).sheet1

    def getAttributeValue(self, attribute):
        cellPosition = self.getCellValue(attribute)

        value = self.sheet.cell(cellPosition[0], cellPosition[1]).value

        return int(value)

    def getSheetName(self):
        with open("driveInformation/characterSheetReference.txt", encoding="utf8") as f:

            for line in f:
                name = re.search(r'\"(.*)\":', line).group(1)
                if name == self.name:
                    return re.search(r':\"(.*)\"', line).group(1)

        raise RuntimeError("The character: " + self.name + " does not have a sheet reference.")

    @staticmethod
    def getCellValue(attribute):
        with open("characterSheetInformation/attributeAndSkillReference.txt", encoding="utf8") as f:

            for line in f:

                current = re.search(r'\"(.*)\"', line)

                if current.group(1) == attribute.lower():
                    row = int(re.search(r'\[(.*),', line).group(1))
                    column = int(re.search(r',(.*)\]', line).group(1))

                    return [row, column]

        raise RuntimeError("The attribute: " + attribute + " does not exists.")
