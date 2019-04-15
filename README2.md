# Prepare Input data

## Crawl persian tweets

## Extract unique tweets
Extract unique tweets from crawled tweets(`--input_file`) and remove mentions and urls and # marks.
```
python3.6 prepare_data.py --get_unique_tweets --input_file ./data/twitter/tweets.iran.txt --output_json_file ./data/twitter/tweets_iran_unique.json
```

## Train
```
python main.py --nhid 64 --seed 123 --data ./data/twitter/tweets_iran_unique.json --loose-json \
        --save output/lang_model_nhid64_ds128/lang_model_nhid64_ds128.pt
```
