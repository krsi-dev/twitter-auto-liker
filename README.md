# Twitter Auto Liker

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@sagocodes.work/how-to-scrape-tweets-and-automatically-like-using-python-faed9d97470b) [![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black) ](https://buymeacoffee/sagocodes) 

![Pasted image 20221022062705](https://user-images.githubusercontent.com/101981345/197374409-b7783e14-47cf-471a-98b3-43a6f691b4af.png)

Using [tweepy](https://tweepy.readthedocs.io/) and [snscrape](https://github.com/JustAnotherArchivist/snscrape/tree/master/snscrape) fetch tweets from a list of twitter usernames and automatically like those tweets.

## Usage

```
$ python main.py --help --ignore--gooey

usage: main.py [-h] yaml_file max_like

positional arguments:
  yaml_file   select file to load
  max_like    maximum like to give per new tweets

options:
  -h, --help  show this help message and exit
```

## YAML

```yaml
---
# Username or name
account: sagocodes

# Twitter API keys
access_token:
access_token_secret: 

consumer_key: 
consumer_secret: 

# List of usernames to track
usernames:
  - python
  - typescript
  - javascript
```

*DISCLAIMER*

*This repository has been created purely for learning purposes. Project maintainers are not responsible if a user gets banned, blocked or be liable for misuse of the tool. Use responsibly.*
