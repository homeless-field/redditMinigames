from random import choice
import json
import praw
reddit = praw.Reddit(user_agent='u/RedditMinigames (by /u/QLZX)', client_id='*', client_secret='*', username='RedditMinigames', password='*')

def higherLower(message, messageBody, subreddit1Name, subreddit2Name, subreddit1Subs, subreddit2Subs):
    prefix = 'If you see this, please message u/QLZX'
    if messageBody.lower() == subreddit1Name.lower() or messageBody.lower() == subreddit2Name.lower():
        if messageBody.lower() == subreddit1Name.lower():
            if subreddit1Subs > subreddit2Subs:
                prefix = 'You win!'
            elif subreddit1Subs < subreddit2Subs:
                prefix = 'You lost :('
        elif messageBody.lower() == subreddit2Name.lower():
            if subreddit1Subs > subreddit2Subs:
                prefix = 'You lost :('
            elif subreddit1Subs < subreddit2Subs:
                prefix = 'You win!'
        if subreddit2Subs == subreddit1Subs:
                prefix = 'You win!'
        prevSubreddit1Name = subreddit1Name
        prevSubreddit1Subs = subreddit1Subs
        prevSubreddit2Name = subreddit2Name
        prevSubreddit2Subs = subreddit2Subs
        with open('subreddits.json', 'r') as subredditsData:
            subreddits = json.load(subredditsData)
            subreddit1 = choice(list(subreddits.keys()))
            subreddit2 = choice(list(subreddits.keys()))
            subreddit1 = [subreddit1, subreddits[subreddit1]]
            subreddit2 = [subreddit2, subreddits[subreddit2]]
        data[author] = {'currentGame': 'higherLower', 'gameStatus': [subreddit1, subreddit2]}
        message.reply(prefix + '(' + prevSubreddit1Name + ': ' + prevSubreddit1Subs + ' / ' + prevSubreddit2Name + ': ' + prevSubreddit2Subs + ')\n\nWhich subreddit has more subscribers? ' + subreddit1[0] + ' or ' + subreddit2[0] + '?')
    else:
        message.reply('Which subreddit has more subscribers? ' + subreddit1Name + ' or ' + subreddit2Name + '?')


for message in reddit.inbox.stream():
    if message in reddit.inbox.unread():
        content = message.body
        author = message.author.name
        with open('userData.json', 'r+') as userData:
            data = json.load(userData)
            if content == 'higherLower':
                with open('subreddits.json', 'r') as subredditsData:
                    subreddits = json.load(subredditsData)
                    subreddit1 = choice(list(subreddits.keys()))
                    subreddit2 = choice(list(subreddits.keys()))
                    subreddit1 = [subreddit1, subreddits[subreddit1]]
                    subreddit2 = [subreddit2, subreddits[subreddit2]]
                data[author] = {'currentGame': 'higherLower', 'gameStatus': [subreddit1, subreddit2]}
                message.reply('Which subreddit has more subscribers? ' + subreddit1[0] + ' or ' + subreddit2[0] + '?')
            elif author not in data:
                message.reply('Please send me a message with only the name of the game you want to play. A list of available games is in the sidebar')
            elif data[author]['currentGame'] == 'higherLower':
                higherLower(message, content, data[author]['gameStatus'][0][0], data[author]['gameStatus'][1][0], data[author]['gameStatus'][0][1], data[author]['gameStatus'][1][1])
            userData.seek(0)
            json.dump(data, userData, indent = 4)
            userData.truncate()
    message.delete()

