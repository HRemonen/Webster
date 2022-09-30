import os

#Folder where all test html files are located.
data_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)))
                    

def get_testdata(*args):
    """
    Get bytes of mock html page for testing purposes.
    """
    path = os.path.join(data_folder, *args)
    
    with open(path, "rb") as f:
        return f.read()
    
def get_testrobots(*args):
    """
    Get content of mock robots.txt file for testing purposes
    """
    path = os.path.join(data_folder, *args)
    
    with open(path, "r") as f:
        return f.read()