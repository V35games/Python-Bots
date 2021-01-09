import praw
import re
from bot import Bot

###########################################################################################################
"""
This file was written and distributed by Vishay Singh, with huge thanks to the fantastic work done 
here: http://pythonforengineers.com/build-a-reddit-bot-part-1/

Please consider visiting the website for further information about the project. 

The bot here runs on the subreddit r/pythonforengineers. Please note that running this bot on any other
subreddit can result in your account being banned for breaking the rules (notably spam). However, if you
want to run the bot on any other subreddit, change line 29 with the desired subreddit.
"""
###########################################################################################################


#a dictionary of mood-quote pairings
bot_quotes = \
{
"calm" : [" That's what I thought. ", " Ok cool.", " nice ;)"],
"mad" : [" No u ", " Blimey mate, don't have feelings of anger towards me because I'm a more dazzing fellow."],
"ironic" : [" The reddit hivemind continues... ", " Have you ever heard the tragedy of Darth Plagueis the Wise?"],
}

#setup reddit
reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("pythonforengineers")

#instantiate Bot
my_bot = Bot("Sir Bottington The Third", bot_quotes)
found_comment = False

#loop through the top five posts in the subreddit's hot section
for submission in subreddit.hot(limit=5):
    if not submission.archived:
        for comment in submission.comments:
            print(comment.body)
            if re.search(".*(IMO)+.*", comment.body, re.IGNORECASE):
                my_bot.change_mood("calm")
                found_comment = True
            elif re.search(".*((left)+(right)*)|((left)*(right)+)+.*", comment.body, re.IGNORECASE):
                my_bot.change_mood("ironic")
                found_comment = True
            elif re.search(".*((you)+((stupid)*(idiot)*(suck)*)+)+.*", comment.body, re.IGNORECASE):
                my_bot.change_mood("mad")
                found_comment = True

            bot_reply = my_bot.get_reply()
            if found_comment:
                comment.reply(bot_reply)
                found_comment = False
                print(bot_reply)
            else:
                print("No valid comment found")   
            


