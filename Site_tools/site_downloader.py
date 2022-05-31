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
    #filename = obj.netloc + obj.path.replace("/", ".")
    filename = "".join([o.replace("/", ".") for o in obj])

    #Check if filename has "." as last char. This is just for the html filetype declaration.
    if filename[-1] == ".":
        filename += "html"
    else: filename += ".html"

    #filepath, pretty explanatory I guess.. 
    filepath = os.path.join(DL_DIR, filename)

    # save the file
    try:
        if not os.path.isfile(filepath):
            # getting the request from url
            r = requests.get(site)

            # create new file and write the html content to it
            with open(filepath, 'w') as file:
                file.write(site+"\n\n")
                file.write("File downloaded: ")
                file.write(NOW.strftime("%d-%m-%Y, %H:%M:%S")+"\n\n")
                file.write(r.text)
                print("File creation succesfull")

        else: raise FileExistsError

    except FileExistsError:
        msg = "File " + filename + " already exists."
        print(msg)


###########################--SETTINGS--###########################

NOW = datetime.now()
DL_DIR = "downloaded/" + NOW.strftime("%m-%d-%Y")

# create folder for this date
__create_project_dir(DL_DIR)

###########################-/SETTINGS/-###########################


if __name__ == "__main__":
    site="https://webscraper.io/test-sites"
    s1 = download_site(site)
    download_site("https://webscraper.io/test-sites/contact")
    