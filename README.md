# Webster

Webster is a python web scraping framework. Simple use, happy days.

## Installation
Install Webster using one off the following methods\
\
Not Implemented\
pip installation incoming\
\
```bash
pip install webster
```
\
From requirements.txt\
```bash
pip install -r requirements.txt
```
\
## Dependencies
Use pipreqs to make new requirements.txt\
if new dependencies are added in PR\
\
```bash
pipreqs --force
```
\
Update dependencies if necessary\
\
```bash
pip install -U -r requirements.txt
```
\
## Testing
Webster uses Unittest for testing.\
\
To run all the tests use the following command:\
\
```bash
python -m unittest discover -v
```
\
Example: We want to test Parser module\
To run single module test use the following command:\
\
```bash
python -m unittest test.test_parser -v
```
\
\
### Coverage
To run test coverage use coverage module\
\
```bash
python -m coverage run -m unittest
```
\
\
## Creating new Crawler instance
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



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
BSD 3-Clause License

Copyright (c) 2022, Henri Remonen.
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.