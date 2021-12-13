import site_downloader
import site_parser
import queue

class Instance:
    def __init__(self) -> None:
        self.queue = queue.Queue()
        self.userInterface()

    def userInterface(self):
        CHOICES = ["s", "d", "p", "e"]
        choices = """
        Choices: 
        (s)ettings
        (d)ownload site
        (p)arse site and create dataset
        (e)xit
        """

        print("""
    Welcome to WebSurfer!
    What would you like to do?""")

        while True:
            print("Main menu.")
            print(choices)
            c = input("Enter choice: ")
            if c.lower() == "e":
                break
            elif c.lower() not in CHOICES:
                print("Incorrect choice, try again")
            elif c == "s":
                self.__settingsMenu()
            elif c == "d":
                self.__downloadMenu()           
            elif c == "p":
                dataset = self.__parseMenu()
                print(dataset)
            else:
                print("Something went wrong.")


    def __settingsMenu(self):
        SETTINGS_CHOICES = ["c", "i", "e"]
        settings_choices = """
        (c)reate queue
        (i)mport queue
        (e)xit
        """
         
        while True:
            print("Settings menu.")
            print(settings_choices)
            c = input("Enter choice: ")
            if c.lower() == "e":
                break
        

    def __downloadMenu(self):
        print("Download menu.")
        site_to_download = input("Enter site URL: ")
        print()

        site_downloader.download_site(site_to_download)

    def __parseMenu(self):
        print("Parse menu.")
        p = site_parser.Parser()
        return p.create_dataset()


#You could start downloading all the associated URLs related to
#the initial sites URL
#for site in data["links"]:
    #site_downloader.download_site(site)

#You could also implement db or something else to store
#the downloaded sites.
if __name__ == "__main__":
    Instance()