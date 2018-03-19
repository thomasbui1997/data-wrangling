#!/usr/bin/env python3
from functools import *
import json
with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)

# TODO: implement assigned functions
    def flatten(xs):
        return reduce(lambda x, y: x+y, xs)

    def difference(xs, ys):
        return list(filter(lambda x: not(x in xs and x in ys), xs+ys))

    def to_text(tweets):
        return list(map(lambda tweet: tweet['content'], tweets))

    def to_lowercase(tweets):
        return list(map(lambda tweet: {**tweet, **{'content': tweet['content'].lower()}}, tweets))

    def nonempty(tweets):
        return filter(lambda x: len(x['content']) > 0, tweets)

    def total_word_count(tweets):
        words_list = map(lambda tweet: tweet['content'].split(), tweets)
        return len(flatten(words_list))

    def hashtags(tweet):
        return list(filter(lambda x: '#' in x, tweet['content'].split()))

    def mentions(tweet):
        return list(filter(lambda x: '@' in x, tweet['content'].split()))

# TODO: counting problems
    def all_hashtags(tweets):
        hashtags_list = list(map(lambda tweet: hashtags(tweet), tweets))
        return flatten(hashtags_list)

    def all_mentions(tweets):
        mentions_list = list(map(lambda tweet: mentions(tweet), tweets))
        return flatten(mentions_list)

    def all_caps_tweets(tweets):
        return filter(lambda tweet: tweet['content'].isupper(), tweets)

    def count_individual_words(tweets):
        word_list = flatten(list(map(lambda tweet: tweet['content'].split(), tweets)))
        return {word: word_list.count(word) for word in word_list}

    def count_individual_hashtags(tweets):
        return {hashtag: all_hashtags(tweets).count(hashtag) for hashtag in all_hashtags(tweets)}

    def count_individual_mentions(tweets):
        return {mention: all_mentions(tweets).count(mention) for mention in all_mentions(tweets)}

    def n_most_common(n, word_count):
        tuple_list = list(word_count.items())
        return sorted(tuple_list, key=lambda k: k[1], reverse = True)[:n]

# TODO: simple filters
    def iphone_tweets(tweets):
        return filter(lambda x: 'iPhone' in x['source'], tweets)

    def android_tweets(tweets):
        return filter(lambda x: 'Android' in x['source'], tweets)

# TODO: statistical analysis
    def average_favorites(tweets):
        favorites_list = list(map(lambda tweet: tweet['favorites'], tweets))
        return round(reduce(lambda x, y: x+y, favorites_list)/len(favorites_list))

    def average_retweets(tweets):
        retweets_list = list(map(lambda tweet: tweet['retweets'], tweets))
        return round(reduce(lambda x, y: x + y, retweets_list) / len(retweets_list))

    def sort_by_favorites(tweets):
        return sorted(tweets, key=lambda tweet: tweet['favorites'])

    def sort_by_retweets(tweets):
        return sorted(tweets, key=lambda tweet: tweet['retweets'])

    def upper_quartile(tweets):
        return tweets[int((len(tweets)-1) * 0.75)]

    def lower_quartile(tweets):
        return tweets[int((len(tweets)-1) * 0.25)]

    def top_quarter_by(tweets, factor):
        return tweets[int((3/4) * len(tweets)):]

    def bottom_quarter_by(tweets, factor):
        return tweets[0:int((1/4) * len(tweets))+1]


print(to_text(android_tweets(tweets)))
