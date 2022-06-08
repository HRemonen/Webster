"""
Helper file for networking related stuff

"""
import requests

def get_http_response(url: str) -> requests.Response:
    """
    Return http response using requests package
    """
    try:
        response = requests.get(url, timeout=2)
        return response
    except requests.RequestException:
        print("Something went wrong requesting page")
    

if __name__ == "__main__":
    s = "https://www.youtube.com/"
    response = get_http_response(s)
    
          