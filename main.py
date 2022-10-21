import json
import yaml
import gooey
import tweepy
import tinydb
from snscrape.modules import twitter

"""
Main application with Gooey
to switch from CLI use --ignore-gooey
"""
@gooey.Gooey(
    # GUI setup
    program_name=f"Twitter Auto Like",
    required_cols=1,
    default_size=(400, 400),
)
def main():
    # Simple JSON database
    database = tinydb.TinyDB("main.json")
    query = tinydb.Query()

    # Gooey parser
    parser = gooey.GooeyParser()

    # Required argument yaml file
    # contains twitter account keys
    # and usernames to scrape tweets from
    parser.add_argument(
        "yaml_file",
        widget="FileChooser",
        help="select file to load"
    )

    # Required integer argument (default: 2)
    # this is the maximum like it will give
    # per account so it doesn't like all tweets
    parser.add_argument(
        "max_like",
        type=int,
        default=2,
        help="maximum like to give per new tweets"
    )

    # Parse arguments
    args = parser.parse_args()

    # Load yaml and parse data
    data = yaml.load(
        open(args.yaml_file, "r"), 
        yaml.loader.SafeLoader)

    # Pretty print data
    print(json.dumps(data, indent=2))
    

    # Twitter client to handle likes
    twitter_client = tweepy.Client(
        access_token=data["access_token"],
        access_token_secret=data["access_token_secret"],
        consumer_key=data["consumer_key"],
        consumer_secret=data["consumer_secret"]
    )

    # Repeat until stopped
    while True:
        # Loop through list of usernames
        for username in data["usernames"]:
            print(f"checking ~ {username}", flush=True)

            # only search for tweets from username
            # excluding retweets and replies
            q = f"from:{username} " + \
                "-filter:retweets " + \
                "-filter:replies  "
                
            # container of tweets parsed
            # so we can keep track of the count
            tweets = []

            # check latest tweets using query
            for tweet in twitter.TwitterSearchScraper(q).get_items():
                # stop if parsed tweets already met max likes
                if len(tweets) == args.max_like:
                    break
                
                # skip if tweet is already parsed
                if database.contains(query.id == tweet.id):
                    continue
                
                # like the tweet
                twitter_client.like(tweet.id, user_auth=True)

                # append to tweets parsed
                tweets.append(tweet.id)
                
                # insert to database so it won't be parsed
                # in the next run
                database.insert({"id": tweet.id})

                print(f"gave a like to ~ {username}", flush=True)
                print(tweet, flush=True)

if __name__ == "__main__":
    main()