
from pymongo import MongoClient

class DatabasePipeline:
    
    collection = "webster"
    
    def __init__(self, db_url: str, db_object: object) -> None:
        self.db_url = db_url
        self.db_object = db_object
    
    @classmethod
    def from_crawler(cls, crawler: object) -> object:
        raise NotImplementedError
        return cls(
            db_url = crawler.settings.MONGO_URL,
            db_object = crawler.settings.MONGO_DB
        )
    
    def open_connection(self) -> None:
        self.client = MongoClient(self.db_url)
        self.connection = self.client[self.db_object]
    
    def close_connection(self) -> None:
        self.client.close()
    
    def feed_database(self, data: dict) -> None:
        self.connection[self.collection].insert_one(data)
        
    