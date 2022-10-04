# Webster

Webster is an experimental python web scraping framework for my own learning.

Webster can be used to scrape or download webpages by giving a list of urls to visit and
optionally a list of urls to stay within.

Webster could be used as a broad crawler also, but it is not optimized for that as of now.

## Version
Webster has been tested using Python 3.8+

## Project documentation
1. [Quick start guide](docs/project_docs/quickstart.md)
2. [Architectural model](docs/project_docs/architecture.md)
3. [Functional specification](docs/project_docs/functional_spec.md)
4. [Test documentation](docs/project_docs/testing.md)
5. Changelog ?

## Examples 

## Installation
Install Webster using one off the following methods

From requirements.txt
```bash
pip install -r requirements.txt
```

### Dependencies
Webster is using multiple external Python packages some of which are:
+ [lxml](https://lxml.de/index.html) used for processing html documents.
+ [w3lib](https://w3lib.readthedocs.io/en/latest/) used for URL handling and prosessing.
+ [pycURL](http://pycurl.io/) used for networking and making requests to a http server.
+ [pymongo](https://pymongo.readthedocs.io/en/stable/) tools for working with mongoDB using python

Use [pipreqs](https://pypi.org/project/pipreqs/) to make new requirements.txt
if new dependencies are added in PR force over requirements.txt
and make sure to include the new one in PR.

```bash
pipreqs --force
```

Update dependencies if necessary

```bash
pip install -U -r requirements.txt
```

## Testing
Webster uses [unittest](https://docs.python.org/3/library/unittest.html) for testing.

To run all the tests use the following command:

```bash
python -m unittest discover -v
```

Example: We want to test Parser module
To run single module test use the following command:

```bash
python -m unittest test.test_parser -v
```


### Coverage
To run test coverage use the [coverage](https://coverage.readthedocs.io/en/6.5.0/) module

```bash
python -m coverage run -m unittest
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