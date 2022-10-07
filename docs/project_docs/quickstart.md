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

### Downloading html documents to disk

Because Webster relies on the Webster.net.Request objects, we can initialize a Downloader instance and download each page to a html file.

Files are stores in the DL_DIR directory defined in settings.
```Python
from webster.core import Downloader
#Bacause Crawler return crawled sites in format:
# {
# url: (webster.net.Request, 
#       [list of adjacent anchors])
# }
#So basically a dictionary where key is the crawled url
#and value is a tuple of Request object and a list of 
#anchors.

#To get the anchors directly
anchors = list(crawled_sites.values())[0][1]
for url in anchors:
        dl = Downloader(req)
        dl.download()


```