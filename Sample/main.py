from wrapper_praw import WrapperPraw

def main():
    wp = WrapperPraw(user_agent=ENV['praw_user_agent'], client_id=ENV['praw_client_id'], client_secret=ENV['praw_client_secret'],
                     username=ENV[reddit_username], password=ENV['reddit-password'], giphy_api_key=ENV['giphy_api_key'])

    # List of subreddits to submit
    wp.start(['reactiongifs'], posts_per_subreddit=1)


if __name__ == '__main__':
    main()
