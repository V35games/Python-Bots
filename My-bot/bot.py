import random

###########################################################################################################
"""
This file was written and distributed by Vishay Singh. The Bot class is to be used by the main.py file.
"""
###########################################################################################################

class Bot:
    """
    A default class for Bot
    """
    def __init__(self, name, quotes):
        """
        The initialisor for an instance of Bot.
        
        <name>: some string representing the bot's name
        
        <quotes>: a dictionary of possible replies that the bot could make. 
        Keys are a string representing the mood of the bot, and values
        are a list of possible responses based on the mood.

        Precondition: name and quotes are non-empty. In addition, quotes must
        contain atleast one key-value pairing with the default mood "calm".

        Postcondition: the mood of a bot will default to "calm" upon 
        initialisation. Use change_mood(mood) to change the mood of the
        bot. The default reply is "<name> says:", unless changed.
        """
        self.name = name
        self.mood = "calm"
        self.quotes = {}
        self.quotes.update(quotes)
        self.reply = self.name + " says:"

    def change_mood(self, mood):
        """
        Updates the current mood of self with <mood>.

        <mood>: a string representing the mood of the bot.
        """
        self.mood = mood
    
    def get_reply(self):
        """
        Returns a response that depends on self's <mood>.
        """
        return self.reply + random.choice(self.quotes.get(self.mood))

