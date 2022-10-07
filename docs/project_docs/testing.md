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


        