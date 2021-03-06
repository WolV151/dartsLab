import threading
import uuid


class MatchRegistry:
    """ Simple in-memory implementation for now: thread-safe"""

    __instance = None

    def __init__(self):
        if MatchRegistry.__instance is not None:
            raise Exception("Singleton class!")
        else:
            MatchRegistry.__instance = self
        self.lock = threading.Lock()
        self.matches = {}
        self.instance = None

    
    @staticmethod
    def get_instance():
        if MatchRegistry.__instance is None:
            with threading.Lock():
                if MatchRegistry.__instance is None:
                    MatchRegistry()
        
        return MatchRegistry.__instance
    
    def add_match(self, match):
        self.lock.acquire()
        match_id = uuid.uuid4() # generate new unique random ID
        self.matches[match_id] = match
        
        return match_id
    
    def get_match(self, match_id):
        return self.matches[uuid.UUID(bytes=match_id)]
    
    