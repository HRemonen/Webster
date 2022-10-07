# Test documentation
Webster testing consists of automated unittesting and integration testing but also manual system testing.

## Unittesting and integration testing
Each class is tested using its own test class. Tests are located in the project [test folder](../../test).

Some classes needs mock data for the test to work, so in the tests folder there is a [subfolder](../../test/test_data) `test_data` which contains a mock site to test `downloader` and `parser` modules.

Current test coverage:

![](static/coverage_report.png)

`Robotstxt` module could not be tested fully, because it does not support local mocking. Because if we give `RobotParser` a website as argument it will try to find it from the internet rather than our `test_data` folder, and that way we cannot test it with our mock site and the mock `robots.txt` file.

## System testing
`Webster` has been also tested thoroughly by hand during the deveploment and before any release. Because automated tests are hard to conduct on live servers.

Objective has been to find any real use bugs or other issues before pushing the release.

`Webster` has been tested on macOS and Linux environments using different user inputted values (including forbidden values), different `Crawler` arguments and different websites.


## Running automated tests
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


## Creating coverage report
To run test coverage use the [coverage](https://coverage.readthedocs.io/en/6.5.0/) module

```bash
python -m coverage run -m unittest
```

To show coverage report in terminal

```bash
python -m coverage report
```

For a nicer report and more detailed use the html report

```bash
python -m coverage html

open htmlcov/index.html   
```