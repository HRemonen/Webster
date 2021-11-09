from genericpath import isfile
import os
import requests

from datetime import datetime
from urllib import parse

def __create_project_dir(directory):
    try:
        os.makedirs(directory)
    except FileExistsError:
        pass

def download_site(site):
    """
    Downloads site content and saves the content as html file.
  
    Parameters:
    site (str): site URL to be downloaded.
  
    Returns:
    None.
  
    """

    obj = parse.urlparse(site)
    filename = obj.netloc + obj.path.replace("/", ".")


    #Check if filename has "." as last char. This is just for the html filetype declaration.
    if filename[-1] == ".":
        filename += "html"
    else: filename += ".html"


    # declare filepath 
    FILEPATH = os.path.join(DOWNLOADED + foldername, filename)


    # save the file
    try:
        if not os.path.isfile(FILEPATH):
            # getting the request from url
            r = requests.get(site)

            # create new file and write the html content to it
            with open(FILEPATH, 'w') as file:
                file.write(site+"\n\n")
                file.write("File downloaded: ")
                file.write(now.strftime("%d-%m-%Y, %H:%M:%S")+"\n\n")
                file.write(r.text)
                print("File creation succesfull")

        else: raise FileExistsError
        
    except FileExistsError:
        msg = "File " + filename + " already exists."
        print(msg)


DOWNLOADED = "downloaded/"
now = datetime.now()
foldername = now.strftime("%m-%d-%Y")

# create folder for this date
__create_project_dir(DOWNLOADED+foldername)


if __name__ == "__main__":
    site="https://webscraper.io/test-sites"
    s1 = download_site(site)
    download_site("https://webscraper.io/test-sites/e-commerce/scroll")
    