from django.core.management.base import BaseCommand
from django.conf import settings

from aspc.activityfeed.models import TwitterActivity

import twitter
import dateutil.parser


class Command(BaseCommand):
    help = 'scrapes latest Tweets and creates SocialMediaActivity objects'

    def handle(self, *args, **options):
        api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
                          consumer_secret=settings.TWITTER_CONSUMER_SECRET,
                          access_token_key=settings.TWITTER_ACCESS_TOKEN,
                          access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET)
        for feedname in settings.TWITTER_FEEDS:
            self.stdout.write("Getting latest tweets from @%s\n" % feedname)
            self.stdout.flush()
            try:
                latest_tweet_id = TwitterActivity.objects.filter(author=feedname)[0].tweet_id
            except:
                latest_tweet_id = ''
            new_tweets = api.GetUserTimeline(screen_name=feedname, since_id=latest_tweet_id,
                                             exclude_replies='true', include_rts='false')
            if new_tweets:
                for tweet in new_tweets:
                    url = 'http://twitter.com/%s/' % feedname
                    content = tweet.text
                    # expand the urls from the t.co shortened versions
                    for urlsub in tweet.urls:
                        content = content.replace(urlsub.url, urlsub.expanded_url)
                    self.stdout.write(("[@%s] %s\n" % (feedname, content)).encode('ascii', 'ignore'))
                    self.stdout.flush()
                    activity = TwitterActivity(url=url, message=content, author=tweet.user.screen_name,
                                               tweet_id=tweet.id, date=dateutil.parser.parse(tweet.created_at))
                    activity.save()
