import time
from random import randint

import giphy_client
from giphy_client.rest import ApiException


class WrapperGiphy:
    def __init__(self, api_key):
        self.api_instance = giphy_client.DefaultApi()
        self.api_key = api_key

    # Return a random link based on the search_word parameter
    def get_link(self, search_word, limit = 50, offset = 0, rating = 'g', lang = 'en', fmt = 'json'):
        try:
            # Connect to API
            api_response = self.api_instance.gifs_search_get(self.api_key, search_word, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)

            # Get gifs
            gifs = api_response.data

            # Return url from a random gif
            random_gif = randint(0, (limit - 1))
            return gifs[random_gif].bitly_gif_url

        except ApiException as e:
            return "Exception gifs_categories_category_get: '{0}'".format(e)
