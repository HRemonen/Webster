# Websurfer

Websurfer is a Python library for downloading pages and crawling websites for information.

## Installation

Install packages using configuration file requirements.txt

To install packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

```python
#Using site downloader:
site="https://example.io/"
s1 = download_site(site)

#or you could just
download_site("https://example.io/contact")
```

--> 
This creates "downloaded" dir inside project folder.
downloaded folder contains directories with name of download date
ex.

+-- project_folder
|
+---+-- downloaded
    |
    +---+-- 11-8-2021  <-- This means the folder was created 8th of november 2021   
        +--  example.io.html
        +--  example.io.contacts.html
        .  
        . 
        .   
+---+-- site_tools
    |
    +-- site_downloader.py
    +-- site_parser.py
+-- README.md
+-- requirements.txt


## License
[MIT](https://choosealicense.com/licenses/mit/)