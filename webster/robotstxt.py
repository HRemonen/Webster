
from urllib import robotparser


class RobotParser():
    
    def __init__(self, root_url: str) -> None:
        self.robotparser = robotparser.RobotFileParser()
        
        #Set the url for robots.txt to the crawler and read it.
        self.robotparser.set_url(root_url)
        self.robotparser.read()
        
    def allowed(self, url: str, user_agent = "*") -> bool:
        """Returns True if the useragent is allowed to fetch the url according 
        to the rules contained in the parsed robots.txt file.

        Args:
            url (str): URL to check if its allowed to scrape.
            user_agent (str, optional): Used user agent. Defaults to "*".

        Returns:
            bool: Boolean value True its fine to crawl. False if not.
        """
        return self.robotparser.can_fetch(user_agent, url)
    
    def delay(self, user_agent = "*") -> None or int:
        """Returns the value of the Crawl-delay parameter from robots.txt 
        for the useragent in question. If there is no such parameter or 
        it doesn’t apply to the useragent specified or the robots.txt 
        entry for this parameter has invalid syntax, return None.

        Args:
            user_agent (str, optional): Used user agent. Defaults to "*".

        Returns:
            None or int: Returns the value of the Crawl-delay parameter from robots.txt
            or None if entry for this parameter is invalid.
        """
        
        return self.robotparser.crawl_delay(user_agent)

