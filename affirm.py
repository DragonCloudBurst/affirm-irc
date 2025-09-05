# reference for code
# https://sopel.chat/docs/plugin

# bot concept: a bot that gives positive affirmations when given a command.

import sopel
from sopel import plugin
import random

affirmations = [
        "you are a good person",
        "you deserve to exist",
        "you are worthwhile",
        "it's okay to take breaks",
        "be kind to yourself",
        "you are not broken",
        "you can get through this",
        "you are strong"
        ] 

cares = [
        "make sure you're drinking water",
        "make sure you're eating",
        "take a shower if you feel icky",
        "give your eyes a break from the screen every now and then",
        ]

@plugin.command('affirm')
def affirm(bot, trigger):
    """ deliver a random quote of affirmation. """
    bot.say(f"{random.choice(affirmations)}")

@plugin.command("care")
def care(bot, trigger):
    """ deliver a random reminder about self-care. """
    bot.say(f"{random.choice(cares)}")
