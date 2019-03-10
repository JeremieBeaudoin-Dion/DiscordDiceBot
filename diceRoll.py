# coding=utf-8
import random


class Dice:
    def __init__(self):
        self.number = 0
        self.numOfDice = 3
        self.typeOfDice = "Chimera"
        self.dSize = 1

        self.msg = ""
        self.goodFormat = True
        self.banter = False

    def getMessage(self):
        return self.msg

    def isChimeraDice(self):
        return self.typeOfDice == "Chimera"

    def isMaxRoll(self):
        return self.banter

    def getAverage(self):
        """This method will return an average if the dice is of type Chimera
            The average will be positive or negative, to see if the player
            rolled under of over what was expected

            EX: I rolled 3 dice. The average should be 3, but I rolled 2.
            getAverage() will return -1"""
        if not self.isChimeraDice:
            return 0

        return self.number - self.numOfDice

    def getNumberOfDice(self):
        return self.numOfDice

    def setNumOfDice(self, numOfDice):
        try:
            self.numOfDice = int(numOfDice)

            if self.numOfDice > 9999:
                self.numOfDice = 9999
        except ValueError:
            self.goodFormat = False

    def setTypeOfDice(self, typeOfDice):
        self.typeOfDice = typeOfDice

    def roll(self):
        if self.typeOfDice == "Chimera":
            self.number = rolld3Dice(self.numOfDice)
            if self.number == 2 * self.numOfDice:
                self.banter = True
        else:
            self.__parse_type_of_dice()
            self.number = rolldXDices(self.dSize, self.numOfDice)
            if self.number == self.dSize * self.numOfDice:
                self.banter = True

        self.__set_message()

    def __parse_type_of_dice(self):
        if self.typeOfDice == "Chimera":
            self.dSize = 3
            return

        try:
            if isinstance(self.typeOfDice, str):
                if self.typeOfDice[0] == "d":
                    self.dSize = int(self.typeOfDice.split("d")[1])
                else:
                    self.dSize = int(self.typeOfDice)
            elif isinstance(self.typeOfDice, int):
                self.dSize = self.typeOfDice
            else:
                self.goodFormat = False

        except ValueError:
            self.goodFormat = False

    def __set_message(self):
        if self.goodFormat:
            if self.typeOfDice == "Chimera":
                self.msg = '{0.author.mention} rolled: **' + str(self.number) + '**\n' + \
                           ' On ' + str(self.numOfDice) + ' Chimera dice'
            else:
                self.msg = '{0.author.mention} rolled: **' + str(self.number) + '**\n' + \
                           ' On ' + str(self.numOfDice) + ' d' + str(self.dSize) + ' dice'

            if self.banter:
                self.msg += '\n :fire: WOOOOOOOOOT MAX ROLL!!!!! :fire:'

        else:
            self.msg = 'I tried to roll dice, but the formatting was wrong :('


def rolld3Dice(numberOfDice):
    value = 0

    while numberOfDice > 0:
        value += rollOned3()
        numberOfDice -= 1

    return value


def rollOned3():
    return random.randint(0, 2)


def rolldXDices(diceSize, numberOfDice):
    value = 0

    while numberOfDice > 0:
        value += rollOneDice(diceSize)
        numberOfDice -= 1

    return value


def rollOneDice(dice):
    return random.randint(0, dice-1) + 1
