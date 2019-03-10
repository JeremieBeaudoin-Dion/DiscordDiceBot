# coding=utf-8
# Work with Python 3.6
import discord
import diceRoll
import diceHistory

TOKEN = '####'

client = discord.Client()

diceHistory = diceHistory.DiceHistory()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!HELP'):
        msg = "Don't worry, everything is going to be fine :)\n".format(message)
        await client.send_message(message.channel, msg)

    content_lowercase = message.content.lower()

    if content_lowercase.startswith('!help'):
        msg = "Type `!hello` for a greeting\n" \
              "Type `!roll` to roll 3 chimera dice\n" \
              "Type `!roll X` to roll X chimera dice\n" \
              "Type `!roll X dX` to roll X dX dice\n" \
              "Type `!stats` to get the statistics of the rolls\n" \
              "Type `!startgame` to reset game stats\n" \
              "Type `!X` and something might happen ;)".format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!test'):
        msg = '1.. 2.. testing... '.format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!x'):
        msg = '{0.author.mention}, by X, I meant anything'.format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!anything'):
        msg = '... not... whatever...'.format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!marco'):
        msg = "Polo!".format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!west'):
        msg = "Marches!".format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!reset') or content_lowercase.startswith('!startgame'):
        diceHistory.reset()
        msg = "Ok, I'll reset the statistics :chart_with_upwards_trend:"
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!stats') or content_lowercase.startswith('!statistics'):
        msg = diceHistory.getStats().format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!roll'):
        words = message.content.split(" ")

        dice = diceRoll.Dice()

        if len(words) == 2:
            dice.setNumOfDice(words[1])

        if len(words) == 3:
            dice.setNumOfDice(words[1])
            dice.setTypeOfDice(words[2])

        dice.roll()

        diceHistory.addDice(dice)

        msg = dice.getMessage().format(message)

        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
