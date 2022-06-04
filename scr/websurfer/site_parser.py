import validators
from urllib.parse import urlparse

class Parser:
    def __init__(self, soup, filepath):
        self.soup = soup
        self.filepath = filepath
        
    def get_base_url(self):
        # read URL from the file downloaded
        with open(self.filepath, "r") as f:
            base_url = urlparse(f.readline().strip())
        
        # get the base url for the relative URLs to work correctly
        result = '{uri.scheme}://{uri.netloc}/'.format(uri=base_url)
        
        return result

    def parse_anchors(self):
        """
        Parse html file for all the links 
    
        Parameters:
        None.
    
        Returns:
        List of URLs.
        """
        anchors = []
        urls = []

        # check base url from downloaded file.      
        base_url = self.get_base_url()
        
        # find every <a> tag from file, with href attribute.
        # store these anchors to a list
        for a in self.soup.find_all("a"):
            anchor = a.attrs['href'] if "href" in a.attrs else ''
            if anchor.startswith("/"):
                # strip the first / from the URL to prevent "//"
                anchors.append(anchor[1:])

            #if anchor is URL istead of relative path add it to the urls list.
            elif validators.url(anchor):
                urls.append(anchor)

        # if the file had any anchors, combine these 
        # directories with base url.
        if anchors:
            for a in anchors:
                url = base_url + a
                if url in urls:
                    continue
                urls.append(url)

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
