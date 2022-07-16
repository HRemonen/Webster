"""
Helper file for URL related stuff

"""
from urllib.parse import urlparse


def URLnetloc(url: str) -> str:
    """
    Get websites URL netloc from the URL string.

    Returns
    -------
    string
        Base URL (<netloc>)
    
    """
    url = urlparse(url)
        
    netloc = '{uri.netloc}'.format(uri=url)
        
    return netloc
