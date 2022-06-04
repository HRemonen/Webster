import validators
from urllib.parse import urlparse

class Parser:
    """
    A class that represents Parser module used to parse 
    downloaded webpages (html files). Proceeds to create a dataset
    of said parse data.
    Module consists of different class methods used to accomplish this.
    
    
    Attributes
    ----------
    soup : object
        Beatifulsoup instance
    filepath : str
        Filepath of the file user wants to parse data out of.
        User defines filepath with filedialog.
    
    Methods
    -------
    get_base_url()
        "Import" websites base URL (URL netloc) from the downloaded file.
        Downloaded files have the URL written on the first rows, along with
        other download information.
        
    parse_anchors()
    
    create_dataset()
    
    """
    def __init__(self, soup: object, filepath: str):
        self.soup = soup
        self.filepath = filepath
        
    def get_base_url(self) -> str:
        """
        "Import" websites base URL (URL netloc) from the downloaded file.
        Downloaded files have the URL written on the first rows, along with
        other download information.
    
        Parameters
        ----------
        None.
        
        Raises
        ------
        None.
    
        Returns
        -------
        string
            Base URL (<scheme>://<netloc>/)
        
        Clarification:
        scheme: The protocol name, usually http(s)://
        netloc: Contains the network location. Includes the domain itself and
        the port number
    
        """
        #read site URL from the file downloaded.
        with open(self.filepath, "r") as f:
            base_url = urlparse(f.readline().strip())
        
        #Get the "base URL" for the relative URLs to work correctly
        #Base URL consist of URL scheme and netloc basically, ignore anything else.
        result = '{uri.scheme}://{uri.netloc}/'.format(uri=base_url)
        
        return result

    def parse_anchors(self) -> list:
        """
        Parses the downloaded html file for URL anchors leading to different 
        sites or sub domains.   
        
        Parameters
        ----------
        None.
        
        Raises
        ------
        None.
    
        Returns
        -------
        list
            a list of parsed anchors, or subURLs found in the website.
    
        """
        
        urls = []

        # check base url from downloaded file.      
        base_url = self.get_base_url()
        
        # find every <a> tag from file, with href attribute.
        # store these anchors to a list
        for a in self.soup.find_all("a"):
            anchor = a.attrs['href'] if "href" in a.attrs else ''
            
            #if anchor start with / it means it is relative path or sub domain
            if anchor.startswith("/"):
                #strip the first / from the URL to prevent "//" that would crash program
                """
                anchors.append(anchor[1:])
                """
                #combine base URL and anchor to make legit URL
                
                ######would there be a better way of doing this and possibly saving
                ######resources?
                url = base_url + anchor[1:]
                if url in urls:
                    continue
                urls.append(url)

            #if anchor is URL istead of relative path add it to the urls list.
            elif validators.url(anchor):
 
                urls.append(anchor)
                
        """ Replaced in version 0.2 to save resources, maybe dont delete yet.
        # if the file had any anchors, combine these 
        # directories with base url.
        
        if anchors:
            for a in anchors:
                url = base_url + a
                if url in urls:
                    continue
                urls.append(url)
        """
        return urls


    def create_dataset(self):
        """
        Creates dataset of chosen html file
    
        Parameters:
        None.
    
        Returns:
        Dictionary dataset.
        """
        try:
            keywords = self.soup.find("meta", 
                attrs={"name" : "keywords"}).get("content")
        except AttributeError:
            keywords = ""
        
        try:
            description = self.soup.find("meta", 
                attrs={"name" : "description"}).get("content")
        except AttributeError:
            description = ""

        dataset = {
            "filepath" : self.filepath,
            "website URL" : self.get_base_url(),
            "title" : self.soup.title.string,
            "keywords" : keywords.split(",") if keywords else None,
            "description" : description if description else None,
            "URLs" : self.parse_anchors()
        }

        return dataset

if __name__ == "__main__":
    p = Parser()
    print(p.create_dataset())
