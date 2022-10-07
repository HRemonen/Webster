# Architectural model
This document describes the architecture of `Webster`.
## Overview
Diagram below shows an overview of Websters achitecture including its components and how data and control flows inside the framework.

![](static/Screenshot%202022-10-04%20at%2013.05.39.png)

## Structure
Quick explanation of each component and its core application.

### Crawler
`Crawler` receives list of urls from the user and feeds these urls into the parser module. `Crawler` also keeps track wether an url has already been crawled, enforcing the `robots.txt ` standard, and if the url is allowed to crawl.

`Crawler` communicates with every other component, so it is basically the brains befind all functions.

When `Crawler` has nothing to crawl it will stop and return the crawled `request` objects.

### Request
`Crawler` calls request module and initializes an `Request` object of given url. `Request` object then calls for its `get` method to fetch the website content and stores it inside a variable along with other information.

`Webster` relies heavily on `Request` objects. They are used in `Crawler`, `Parser` and `Downloader` modules.

### Parser
`Crawler` receives `Request` object from the request module. Then Crawler checks if the request can be reused for parsing. If that is the case, `Crawler` feeds the `Request` object to `Parser` module which parses all adjacent anchors it finds of given request (or website).

`Parser` returns found anchors back to the `Crawler`, which then proceeds to request these anchors again and again until no more is found.

### Downloader
`Downloader` receives `Request` object from the `Crawler` and downloads the website in html format that is related to the Request object.

`Downloader` stores these downloaded files in a user defined directory found in `settings`.

### Database pipeline
Database pipeline is in charge of storing given `Request` objects to the `database`. `Webster` uses `MongoDB` as its `database`, thought it is not necessary to use `database` at all if not wanted.
User can define own `MongoDB` connection settings in the `settings` file.

Parser has method for creating dataset, that can then be stored in to the database.

Database connection is still work in progress.
