# Prepare Input data

## Crawl persian tweets

## Extract unique tweets
Extract unique tweets from crawled tweets(`--input_file`) and remove mentions and urls and # marks.
```
python3.6 prepare_data.py --get_unique_tweets --input_file ./data/twitter/tweets.iran.txt --output_json_file ./data/twitter/tweets_iran_unique.json
```
