# Quickstart guide

### Creating new Crawler instance
```python
from webster.crawler import Crawler

#Make a list of websites to start crawling from.
#Atleast provide 1 starting URL.
sites = [ 
        "https://site1.io",
        "https://site2.io", 
        "https://site3.io", 
        ]

#Define allowed urls to scrape (Optional):
#If no allowed urls are provided the crawler 
#starts wide crawls. Meaning it wont stop 
#until there is no more sites

allowed = ["https://site.io"]
    
# Create new Crawler instance:
my_crawler = Crawler(
                sites, 
                allowed_urls=allowed
            )

```
### Crawling

Now that the Crawler is configured start crawling.
Crawler returns the crawled websites as Webster.net.Request 
objects as dictionary for later use.

```Python
crawled_sites = my_crawler.crawl()
```
