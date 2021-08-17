import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("m3wJBv3OLNHVKsmuzom1jFPvs", "7chJBonDSkBAWtnOrmsH0Jg44kK9155JNxytDmKsi6JRamMRp9")
auth.set_access_token("1348066546464251911-Oqo5VTad4Sp4IkhTWVC62JoHQdIpCZ", "KmSo28iT99yWZcsotrqsX5Q0GygcG6YYV9jJc3mFrJlbI")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#Tweet
api.update_status("Test tweet from Tweepy Python")
