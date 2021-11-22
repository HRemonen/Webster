# Websurfer

Websurfer is a Python library for downloading pages and crawling websites for information.

## Installation

Install packages using configuration file requirements.txt

To install packages using pip:

```bash
pip install -r requirements.txt
```

## Usage 
### site_downloader module

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

```
+-- project_folder
│
+---+-- downloaded
│   │ 
│   +---+-- ex. 11-8-2021
│       │        
│       +--  example.io.html
│       +--  example.io.contacts.html
│       .  
│       . 
│       .   
+---+-- site_tools
│   │
│   +-- site_downloader.py
│   +-- site_parser.py
│   .
│   .
│   .
+-- README.md
+-- requirements.txt
```

### site_parser module

```python
#Creating new site_parser. This opens file navigator to select the file to parse
p = site_parser.Parser()

#Creating the dataset from the file
data = p.create_dataset()

```

#### create_dataset()
```python
#Creates a dataset from the file. This dataset contains:

dataset = {
    "filepath" : string / path, #filepath,
    "website URL" : string, #site url,
    "title" : string, #site title,
    "keywords" : list, #keywords or "None",
    "description" : string, #description or "None",
    "links" : list, #all <a> tag elements in file
    }
```
##### Usage

```python
#For example you could iterate through every link in the file and download the sites:

for site in data["links"]:
    site_downloader.download_site(site)

```

## License
MIT License

Copyright (c) 2021, Henri Juhani Remonen

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.