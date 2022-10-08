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
#Now Crawler instance has been created and is ready to use.

```
### Crawling

Now that the `Crawler` is configured start crawling.
`Crawler` returns the crawled websites as `Request` 
objects as dictionary for later use.

```Python
crawled_sites = my_crawler.crawl()
```

### Downloading Request object as html documents to disk

Because `Webster` relies on the `Request` objects, we can initialize a `Downloader` instance and download each page to a html file.

Files are stores in the `DL_DIR` directory defined in `settings`.

```Python
from webster.core import Downloader
#Bacause Crawler return crawled sites in format:
# {
# url: webster.net.Request 
# }
#So basically a dictionary where key is the crawled url
#and value Request object
#Returned dictionary should cover all the found urls including
#every anchor possible.

#You could iterate over the crawled sites
#using for loop.
#Each Request must have its own Downloader instance.

for url in crawled_sites.values():
        dl = Downloader(req)
        dl.download()

#Downloaded files will appear in the downloaded folder 
#determited in the settings file.
```

### Parsing Request objects

`Webster` allows for reprosessing `Request` objects after crawling.

`Parser` module has `parse_anchors` and `parse_index` methods for prosessing `Request` objects.

Methods can be used in your own code for accomplishing various functionalities.

```Python
for url in crawled_sites.values():
        p = Parser(req)
        
        #To create indices of Requests you can call the method
        #create_index
        indices = p.parse_index()

        #You could either parse anchors by using the method
        #parse_anchors
        anchors = p.parse_anchors()
        #or if you are creating indices, you can just get the
        #anchors using the 'adjacent' key.
        anchors = indices['adjacent']

        yield anchors, indices
```

### Parsing other data

Above is just an example of what you could use `Parser` module for after crawling
`create_index` method creates a dataset used to store crawled sites to databases.
Indices constructs of the following information
```Python
indice = {
            "url": root_url,
            "adjacents": adjacent,
            "title": title,
            "description": description,
            "keywords": kwords,
            "text": content
        }
```
You could parse any of these values after crawling depending on your needs and use them in your code.