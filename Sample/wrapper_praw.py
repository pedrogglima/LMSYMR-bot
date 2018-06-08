from wrapper_giphy import WrapperGiphy
from response import SubmissionResponse

import praw


class WrapperPraw:

    QUESTIONS = ['bliss', 'what', 'when']
    REPLY_TEMPLATE = '[Let me show you my reaction]({})'


    def __init__(self, user_agent, client_id, client_secret, username, password, giphy_api_key):
        self.reddit = praw.Reddit(user_agent=user_agent, client_id=client_id, client_secret=client_secret,
                                 username=username, password=password)
        self.wgiphy = WrapperGiphy(giphy_api_key)


    def start(self, subreddits, posts_per_subreddit):
        for subreddit in subreddits:
            response = SubmissionResponse(subreddit)
            for submission in self.reddit.subreddit(subreddit).stream.submissions(pause_after=0):
                # If stream is put to waiting OR number of submissions >= per sub, then break
                if submission is None or response.count >= posts_per_subreddit:
                    break

                response = self.process_submission(submission, response)


    # Compare submission's title with QUESTIONS, if positive, call submit method.
    def process_submission(self, submission, response):
        response.title = submission.title.lower()

        for question_phrase in self.QUESTIONS:
            if question_phrase in response.title:

                url = self.wgiphy.get_link(question_phrase)
                if "https://" in url:
                    response.url = url
                    response = self.submit(submission, response)
                else:
                    response.failure("Error retrieving gifs url: '{0}'".format(url))

                # After submition's success or failure, exit the loop.
                break

        return response


    # Submit post with gif's url to subreddit
    def submit(self, submission, response):
        reply_text = self.REPLY_TEMPLATE.format(response.url)

        try:
            submission.reply(reply_text)
            response.success()
        except praw.exceptions.APIException as e:
            response.failure(e.message)

        return response
