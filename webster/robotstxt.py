
from urllib import robotparser


class RobotParser():
    
    def __init__(self, root_url: str) -> None:
        self.robotparser = robotparser.RobotFileParser()
        
        #Set the url for robots.txt to the crawler and read it.
        self.robotparser.set_url(root_url)
        self.robotparser.read()
        
    def allowed(self, url: str, user_agent = "*") -> bool:
        
        return self.robotparser.can_fetch(user_agent, url)

