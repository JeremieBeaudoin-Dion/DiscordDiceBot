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
        embed = discord.Embed(color=0xC27BA0)
        embed.add_field(name="Bot Commands",
                        value="Type `!hello` for a greeting\n" \
                              "Type `!roll` to roll 3 chimera dice\n" \
                              "Type `!roll X` to roll X chimera dice\n" \
                              "Type `!roll X dX` to roll X dX dice\n" \
                              "Type `!sroll ____ ` to roll a secret dice. The result will be sent to the GM\n" \
                              "Type `!stats` to get the statistics of the rolls\n" \
                              "Type `!startgame` to reset game stats\n" \
                              "Type `!whisper` to whisper something to the GM\n" \
                              "Type `!about X` to know more about something\n" \
                              "Type `!X` and something might happen ;)", inline=False)

        await client.send_message(message.channel, embed=embed)

    if content_lowercase.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!test'):
        msg = '1.. 2.. testing... '.format(message)
        await client.delete_message(message)
        await client.send_message(client.get_channel(id='####'), msg)  # send to Robot test

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
        msg = "Ok, I'll reset the statistics :chart_with_upwards_trend:".format(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!stats') or content_lowercase.startswith('!statistics'):
        embed = discord.Embed(color=0xC27BA0)
        embed.add_field(name="Last Game's Statistics",
                        value=diceHistory.getStats(), inline=False)

        await client.send_message(message.channel, embed=embed)

    if content_lowercase.startswith('+'):
        pass

    if content_lowercase.startswith('!sroll'):
        msg = roll_dice(message)
        author = message.author

        await client.delete_message(message)
        await client.send_message(author, msg)  # Send to author
        await client.send_message(get_gm(), msg)  # Send to game master

    if content_lowercase.startswith('!whisper'):

        msg = message.content.replace("!whisper", "")
        msg = "Whisper: \n `" + msg + "`\n by " + str(message.author)
        msg = msg.format(message)

        await client.delete_message(message)
        await client.send_message(get_gm(), msg)  # Send to game master

    if content_lowercase.startswith('!delete'):
        await client.delete_message(message)

    if content_lowercase.startswith('!roll'):
        msg = roll_dice(message)
        await client.send_message(message.channel, msg)

    if content_lowercase.startswith('!about'):
        msg = "-" + message.content.replace("!about ", "")
        await client.send_message(message.channel, msg)


def roll_dice(message):
    words = message.content.split(" ")

    dice = diceRoll.Dice()

    if len(words) == 2:
        dice.setNumOfDice(words[1])

    if len(words) == 3:
        dice.setNumOfDice(words[1])
        dice.setTypeOfDice(words[2])

    dice.roll()

    diceHistory.addDice(dice)

    return dice.getMessage().format(message)


def get_gm():
    return discord.utils.get(client.get_all_members(), id='####')


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    # Set status as "playing Chimera"
    await client.change_presence(game=discord.Game(name="Chimera | !help"))


client.run(TOKEN)
