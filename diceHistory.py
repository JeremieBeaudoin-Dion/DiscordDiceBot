import diceRoll


class DiceHistory():
    def __init__(self):
        self.allDice = []

    def addDice(self, dice):
        self.allDice.append(dice)

    def reset(self):
        self.allDice = []

    def getStats(self):
        number_total = 0
        number_chimera = 0
        number_of_other_dice = 0

        maxRolls = 0
        avg = 0

        avg_number_if_dice = 0

        for dice in self.allDice:
            number_total += dice.getNumberOfDice()

            if dice.isChimeraDice():
                curr_avg = dice.getAverage()

                avg += curr_avg
                number_chimera += 1

                if curr_avg > 0:
                    avg_number_if_dice += 1

                if curr_avg < 0:
                    avg_number_if_dice -= 1
            else:
                number_of_other_dice += dice.getNumberOfDice()

            if dice.isMaxRoll():
                maxRolls += 1

        if avg >= 0:
            sign = "+"
        else:
            sign = ""

        return ":game_die:" + str(number_total) + " dice were rolled in " + str(len(self.allDice)) + " throws \n" + \
               str(number_of_other_dice) + " of which were special dice \n" \
               "On average, you rolled " + sign + str(avg) + " over the expected outcome \n" \
               "Which is " + str(avg_number_if_dice) + " throws over the mean \n"\
               "And there were " + str(maxRolls) + " max rolls! :fire:"


def test():
    dice1 = diceRoll.Dice()
    dice1.roll()

    dice2 = diceRoll.Dice()
    dice2.setTypeOfDice("d2")
    dice2.setNumOfDice(5)
    dice2.roll()

    dice3 = diceRoll.Dice()
    dice3.number = 6
    dice3.banter = True

    dh = DiceHistory()
    dh.addDice(dice1)
    dh.addDice(dice2)
    dh.addDice(dice3)

    print(dh.getStats())

def test2():

    for x in range(10):
        dh = DiceHistory()
        for i in range(200000):
            dice = diceRoll.Dice()
            dice.roll()
            dh.addDice(dice)

        print(dh.getStats())


