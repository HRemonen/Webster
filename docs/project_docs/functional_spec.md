# Functional specification
## Objective
Objective is to make a lightweight web crawling framework that is simple and easy to use. Webster is aimed to be used as a web scraping framework by independent software developers. Webster is remaining as an open source project and free to use for all within the license.

## Users
In this document independent software developers are referred as the users. Users can use this web scraping framework as part of their own software. Webster does not predefine any strict use cases, it is meant to be a tool.

Use cases include crawling and storing indices of given webpages. User can then use the crawled indices to parse usefull information wanted. Users are responsible to enforce GDPR or any other privacy laws.

## Features
+ Able to give a list or URLs to scrape from. Atleast one URL has to be given to be able to start crawling.
+ Able to restrict the URLs to scrape. Crawler takes a list of URL to allow scraping. Any URL not matching these are considered out of boundaries and not processed.
+ Obeys robots.txt standard by default. When encountering new URL crawler checks what is allowed and what is not. Users may change this at own risk in the settings and conduct crawls ignoring this standard. Not recommended.
+ Crawler parses all adjacent anchors from given URL and proceeds to crawl all of the found anchords. When a page is requested and parsed, a predefined dataset is stored inside database. Webster also comes with a downloader module, which could be used to physically download the html page and store in memory. Both are also possible simultaneously.

## Further development
+ Crawl function in Webster.crawler.py should be a generator object, so that users could pull the next request when needed.
+ User should be able to terminate a crawler instance gracefully at any given time.
+ Threading, while also enforcing robots.txt.
+ Logging on all modules.
+ pip install.


