# AityBot
Aityz's Discord Bot is a versatile bot, with a variety of use cases. Feel free to clone/make a pull request and modify is as you need.
## Features
AityBot currently has the following features:
- Reddit (or Kbin/Lemmy etc.) like Karma system (upvotes and downbotes and /karma to check total)
- Geocoding Support (/geocode for any location)
- Pokemon Loot Table (WIP, not currently high priority)
- Reddit Data API Integration (WIP)
- Reddit Page .JSON Support
- OpenWeatherMap Support (/weather for weather)
- NewsAPI Intergration (/news for headlines)
- Integrations with Many APIs (WIP)
- Gradio interconnectivity with Hugging Face Spaces (see /gpt2eli5 for an example)
## Setting Up
AityBot is very easy to set up. First clone `git clone https://github.com/Aityz/AityBot.git` and then create a python file called `confidential.py`. Create variables called TOKEN, NEWSAPI, OPENWEATHERMAP, REDDITCLIENT and REDDITSECRET and make the values the tokens of the respective APIs. REDDITREFRESH must be the Refresh Token of a Reddit Account. PUBKEY and PRIKEY are RSA Encryption Keys.
## Encryption
AityBot is planning to use Oath2 URLs and therefore requires encrypting the refresh tokens etc. AityBot uses RSA encryption keys (specified in confidential.py).