import unittest
import analyze


class MyTestCase(unittest.TestCase):

    def test_flatten(self):
        assert analyze.flatten([[1, 2], [], [3, 4]]) == [1, 2, 3, 4]

    def test_difference(self):
        assert analyze.difference([1, 2], [2, 3]) == [1, 3]

    def test_to_text(self):
        tweet1 = {"content": "My hands are YUUGE!"}
        tweet2 = {"content": "#MAGA"}
        tweet3 = {"content": "I hate Little Marco."}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.to_text(tweets) == ["My hands are YUUGE!", "#MAGA", "I hate Little Marco."]

    def test_to_lowercase(self):
        tweet1 = {"content": "My hands are YUUGE!", 'hey': 'yo'}
        tweet2 = {"content": "#MAGA"}
        tweet3 = {"content": "I hate Little Marco."}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.to_text(analyze.to_lowercase(tweets)) == ["my hands are yuuge!", "#maga", "i hate little marco."]

    def test_non_empty(self):
        tweet1 = {"content": "#MAGA"}
        tweet2 = {"content": ""}
        tweet3 = {"content": "#CrookedHillary"}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.to_text(analyze.nonempty(tweets)) == ["#MAGA", "#CrookedHillary"]


    def test_total_word_count(self):
        tweet1 = {"content": "I am President now."}
        tweet2 = {"content": "Make America Safe Again!"}
        tweet3 = {"content": "Make America Great Again!"}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.total_word_count(tweets) == 12

    def test_hashtags(self):
        tweet = {"content": "Hello, America. #MAGA #Trump2016"}
        assert analyze.hashtags(tweet) == ["#MAGA", "#Trump2016"]

    def test_mentions(self):
        tweet = {"content": "@aatxe would be a better president than me. "}
        assert analyze.mentions(tweet) == ["@aatxe"]

    def test_all_hashtags(self):
        tweet1 = {"content": "Hello, America. #MAGA #Trump2016"}
        tweet2 = {"content": "Lock her up! #CrookedHillary #MAGA"}
        tweet3 = {"content": "No hashtags in here."}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.all_hashtags(tweets) == ["#MAGA", "#Trump2016", "#CrookedHillary", "#MAGA"]

    def test_all_mentions(self):
        tweet1 = {"content": "@cnn is fake news!"}
        tweet2 = {"content": "Can’t believe how many people buy @cnn fake news!"}
        tweet3 = {"content": "@marcorubio and I are friends now!"}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.all_mentions(tweets) == ["@cnn", "@cnn", "@marcorubio"]

    def test_all_caps_tweets(self):
        tweet1 = {"content": "MAKE AMERICA SAFE AGAIN!"}
        tweet2 = {"content": "Can’t believe how many people buy @cnn fake news!"}
        tweet3 = {"content": "AMERICA FIRST!"}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.to_text(analyze.all_caps_tweets(tweets)) == ["MAKE AMERICA SAFE AGAIN!", "AMERICA FIRST!"]

    def test_count_individual_words(self):
        tweet1 = {"content": "MAKE AMERICA SAFE AGAIN!"}
        tweet2 = {"content": "america"}
        tweet3 = {"content": "AMERICA FIRST!"}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.count_individual_words(tweets) == {"MAKE": 1, "AMERICA": 2, "SAFE": 1, "AGAIN!": 1, "FIRST!": 1,
                                                          "america": 1}

    def test_count_individual_hashtags(self):
        tweet1 = {"content": "#MAGA #Trump2016"}
        tweet2 = {"content": "#MakeAmericaGreatAgain"}
        tweet3 = {"content": "No hashtags in here."}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.count_individual_hashtags(tweets) == {"#MAGA": 1, "#Trump2016": 1, "#MakeAmericaGreatAgain": 1}

    def test_count_individual_mentions(self):
        tweet1 = {"content": "@cnn is fake news!"}
        tweet2 = {"content": "Can’t believe how many people buy @cnn fake news!"}
        tweet3 = {"content": "@marcorubio and I are friends now!"}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.count_individual_mentions(tweets) == {"@cnn": 2, "@marcorubio": 1}

    def test_n_most_common(self):
        tweet1 = {"content": "MAKE AMERICA SAFE AGAIN!"}
        tweet2 = {"content": "america"}
        tweet3 = {"content": "AMERICA FIRST!"}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.n_most_common(1, analyze.count_individual_words(tweets)) == [("AMERICA", 2)]

    def test_iphone_tweets(self):
        tweet1 = {"content": "My hands are YUUGE!", "source": "Twitter for iPhone"}
        tweet2 = {"content": "#MakeAmericaOkAgain", "source": "Twitter for Android"}
        tweet3 = {"content": "#CrookedHillary", "source": "Twitter for iPhone"}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.to_text(analyze.iphone_tweets(tweets)) == ["My hands are YUUGE!", "#CrookedHillary"]

    def test_android_tweets(self):
        tweet1 = {"content": "My hands are YUUGE!", "source": "Twitter for iPhone"}
        tweet2 = {"content": "#MakeAmericaOkAgain", "source": "Twitter for Android"}
        tweet3 = {"content": "I hate Little Marco.", "source": "Twitter for iPhone"}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.to_text(analyze.android_tweets(tweets)) == ["#MakeAmericaOkAgain"]

    def test_average_favorites(self):
        tweet1 = {"favorites": 32}
        tweet2 = {"favorites": 8}
        tweet3 = {"favorites": 16}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.average_favorites(tweets) == 19

    def test_average_retweet(self):
        tweet1 = {"retweets": 32}
        tweet2 = {"retweets": 80}
        tweet3 = {"retweets": 16}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.average_retweets(tweets) == 43

    def test_sort_by_favorites(self):
        tweet1 = {"favorites": 32}
        tweet2 = {"favorites": 8}
        tweet3 = {"favorites": 16}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.sort_by_favorites(tweets) == [tweet2, tweet3, tweet1]

    def test_sort_by_retweets(self):
        tweet1 = {"retweets": 32}
        tweet2 = {"retweets": 8}
        tweet3 = {"retweets": 16}
        tweets = [tweet1, tweet2, tweet3]
        assert analyze.sort_by_retweets(tweets) == [tweet2, tweet3, tweet1]

    def test_upper_quartile(self):
        tweet1 = {"favorites": 32}
        tweet2 = {"favorites": 8}
        tweet3 = {"favorites": 16}
        tweet4 = {"favorites": 19}
        tweet5 = {"favorites": 44}
        tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]
        assert analyze.upper_quartile(analyze.sort_by_favorites(tweets)) == tweet1

    def test_lower_quartile(self):
        tweet1 = {"retweets": 32}
        tweet2 = {"retweets": 8}
        tweet3 = {"retweets": 16}
        tweet4 = {"retweets": 19}
        tweet5 = {"retweets": 44}
        tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]
        assert analyze.lower_quartile(analyze.sort_by_retweets(tweets)) == tweet3

    def test_top_quarter_by(self):
        tweet1 = {"retweets": 32}
        tweet2 = {"retweets": 8}
        tweet3 = {"retweets": 16}
        tweet4 = {"retweets": 19}
        tweet5 = {"retweets": 44}
        tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]
        assert analyze.top_quarter_by(analyze.sort_by_retweets(tweets), "retweets") == [tweet1, tweet5]

    def test_bottom_quarter_by(self):
        tweet1 = {"favorites": 32}
        tweet2 = {"favorites": 8}
        tweet3 = {"favorites": 16}
        tweet4 = {"favorites": 19}
        tweet5 = {"favorites": 44}
        tweets = [tweet1, tweet2, tweet3, tweet4, tweet5]
        analyze.bottom_quarter_by(analyze.sort_by_favorites(tweets), "favorites") == [tweet2, tweet3]



if __name__ == '__main__':
    unittest.main()
