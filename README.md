# LMSYMR Bot

Entertainment script bot wrote in Python that works on [Reddit](https://reddit.com/).

LMSYMR answers to posts on subreddits with gifs (link to) based on key-words found on post's title.
The bot uses Giphy's search engineer to find appropriate gifs based on key-words.
The bot can be configurable about searching key-words and number of posts per subreddit.

<hr />

### Requirements

 * Python3
 * [Create/Have account on Reddit](https://reddit.com/)
 * [Sign in to Giphy API](https://developers.giphy.com/)

### Dependencies

 * [Praw](https://github.com/praw-dev/praw)
 * [Giphy client](https://giphy.com/)

### Install

`cd ~/some/dir`  
`git clone https://github.com/pedrogglima/LMSYMR-bot.git`

### Uninstall

`rm -rf ~/some/dir/LMSYMR-bot`

### How to use it:

The bot uses Praw API to connect and interect with Reddit, and Giphy API to search and generate links to the gifs. So, to use both API's the follow
personal information will be necessary:

 * User Agent: short description about the bot (i.g 'awnser questions with gifs u/YOUR-REDDIT-USERNAME'.
 * Client id: Will be given after you set up your Reddit account.
 * Client secret: Will be given after you set up your Reddit account.
 * Reddit username: Your reddit's username.
 * Reddit password: Your reddit's password.
 * Giphy API key: This key will be given to you when you create your account on [Giphy API](https://developers.giphy.com/).

To get `Client id` and `Client secret` you must log in in your Reddit account, then go to preferences > apps > create an app, and fill up the form. After getting the personal information, you can add them to the file `sample/main.py`.

To set the subreddits that you want the bot post on, go to `sample/main.py` and add the names to the list of subreddits names. You can also set the number of posts per subreddit on this same file.

To set the key-words that the Bot will be using to search and post on user's posts, go to `sample/wrapper_praw.py` and add the words to the constant QUESTION
in the beginning of the file.  

To monitoring the bot activities, you can check the log on `sample/output.log`.  

The bot is not set to work periodically, to do that you could create a cron job on your machine and call the `sample/main.py`.  

For the last, if you don't have karma points (users reputation on Reddit) you may not be able to post on certain subreddit. Also, the Praw API (Reddit) has a limit of posts per user. For this last one, the bot is set automatic to wait 10 minutes after each post made.


### Contributing:

Patches are welcome! Fork, hack, request pull! Here is my current to-do list:

 * Improve the heuristics to the key-words used to find gifs
 * Add functionalities as: set cron jobs to the bot, more user-friendly features and others.

### Licenses and Copyright

Copyright (C) 2018 Pedro Gabriel Lima.  

License GPLv3+: GNU GPL version 3 or later http://gnu.org/licenses/gpl.html.  

This is free software: you are free to change and redistribute it.  

There is NO WARRANTY, to the extent permitted by law.  
