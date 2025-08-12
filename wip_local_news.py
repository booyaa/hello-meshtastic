from rss_parser import RSSParser
from requests import get  # noqa

rss_url = "https://feeds.bbci.co.uk/news/england/norfolk/rss.xml"
response = get(rss_url)

rss = RSSParser.parse(response.text)

# Print out rss meta data
print("Language", rss.channel.language)
print("RSS", rss.version)

# Iteratively print feed items
for item in rss.channel.items:
    print(item.title.content)
    print(item.description.content[:45])

# 5 (bong) + title (100) + url (50) = 155, leaves you how many characters if the limit is 200?
print(200 - 5 - 100 - 50)
