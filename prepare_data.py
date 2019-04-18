# -*- coding: utf-8 -*-
import re
import json
import argparse


def get_unique_tweets(input_file, output_file):
    tweet_ids = set()
    retweet_ids = set()
    retweet_tweet_map = {}
    with open(input_file, encoding='utf8') as f:
        for line in f:
            try:
                tweet = json.loads(line)
                if "retweeted_status" in tweet:
                    retweet_ids.add(tweet["id_str"])
                    retweet_tweet_map[tweet["id_str"]] = tweet["retweeted_status"]["id_str"]
                else:
                    tweet_ids.add(tweet["id_str"])
            except:
                print("Error happened while reading this line:", line)
                continue
    print("\nWe have %i tweets and %i retweet" % (len(tweet_ids), len(retweet_ids)))

    # Do we have all tweets of retweets?
    retweet_without_tweet = set()
    for retweet_id in retweet_ids:
        tweet_id = retweet_tweet_map[retweet_id]
        if tweet_id not in tweet_ids:
            retweet_without_tweet.add(retweet_id)
    print("\nWe have %i retweets which don't have their tweets" % (len(retweet_without_tweet)))

    with open(input_file, encoding='utf8') as f:
        with open(output_file, 'w', encoding='utf8') as out:
            for line in f:
                try:
                    tweet = json.loads(line)
                    if tweet["id_str"] not in tweet_ids and tweet["id_str"] not in retweet_without_tweet:
                        continue

                    if tweet["id_str"] in tweet_ids:
                        tweet_id = tweet["id_str"]
                        tweet_text = tweet["full_text"].replace("\n", " ").replace("\r", " ")
                    elif tweet["id_str"] in retweet_without_tweet:
                        tweet_id = tweet["retweeted_status"]["id_str"]
                        tweet_text = tweet["retweeted_status"]["full_text"].replace("\n", " ").replace("\r", " ")
                    text = re.sub(r"(?:\@|https?\://)\S+", "", tweet_text)
                    text = text.replace("\"", "").replace("\'", "").replace("\\", "")
                    search_results = re.findall(r"#(\w+)", text)
                    for hashtag in search_results:
                        text = text.replace(hashtag, hashtag.replace("_", " "))
                    text = text.replace("#", "")
                    out.write(json.dumps({"id": tweet_id, "sentence": text}, ensure_ascii=False) + "\n")
                except:
                    print("Error happened while reading this line:", line)
                    continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--get_unique_tweets', help='extract unique set of tweets', action='store_true')
    parser.add_argument('--input_file', help='Path to the input file')
    parser.add_argument('--output_json_file', help='Path to the output json file')
    args = parser.parse_args()

    if args.get_unique_tweets:
        get_unique_tweets(args.input_file, args.output_json_file)
