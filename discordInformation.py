
def getToken():
    with open("discordInformation/token.txt", encoding="utf8") as f:
        for line in f:
            return line


def getGMKey():
    with open("discordInformation/gameMasterKey.txt", encoding="utf8") as f:
        for line in f:
            return line
