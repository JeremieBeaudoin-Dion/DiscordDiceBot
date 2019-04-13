import re

from sheetReader import CharacterSheet


class Holder:
    def __init__(self):
        self.characters = {}

        for name in self.__getAllCharNames():
            self.characters[name] = CharacterSheet(name)

    @staticmethod
    def __getRefToCharacterName(discordName):
        with open("discordInformation/characterDiscordReference.txt", encoding="utf8") as f:
            for line in f:
                discId = re.search(r'\"(.*)\":', line).group(1)

                if discId == discordName:
                    return re.search(r':\"(.*)\"', line).group(1)

        raise RuntimeError("The discordName " + discordName + " does not appear to have a character associated with it")

    @staticmethod
    def __getAllCharNames():
        allNames = []

        with open("discordInformation/characterDiscordReference.txt", encoding="utf8") as f:
            for line in f:
                allNames.append(re.search(r':\"(.*)\"', line).group(1))

        return allNames

    @staticmethod
    def isAnAttribute(attribute):
        with open("characterSheetInformation/attributeAndSkillReference.txt", encoding="utf8") as f:

            for line in f:

                current = re.search(r'\"(.*)\"', line)

                if current.group(1) == attribute.lower():
                    return True

        return False

    def getAttribute(self, discordName, attrName):
        return self.characters[self.__getRefToCharacterName(discordName)].getAttributeValue(attrName)

