import site_downloader
import site_parser
import queue

class WebSurfer:
    def __init__(self) -> None:
        self.queue = queue.Queue()
        self.autoQueue = False
        self.userInterface()

    def userInterface(self):
        CHOICES = ["s", "d", "p", "e"]
        print("""
        Welcome to WebSurfer!
        What would you like to do?
        """)

        while True:
            print("Main menu.")
            print("""
            Choices:
            (s)ettings
            (a)uto downloader
            (d)ownload site                     (manual)
            (p)arse site and create dataset     (manual)
            (e)xit
            """)

            c = input("Enter choice: ").lower()
            if c == "e":
                break
            elif c not in CHOICES:
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

        #Implement queue for URLs.
        #user can create queue manually typing each URL seperately or
        #user could also import queue from text file or
        #user could also create queue from dataset urls.
         
        while True:
            settings_choices = f"""
            (c)reate queue manually
            (i)mport URLs from text file
            (t)oggle autodownloader queing      {self.autoQueue}
            (e)xit
            """
            print("Settings menu.")
            print(settings_choices)

            c = input("Enter choice: ").lower()
            if c == "e":
                break
            elif c == "t":
                self.autoQueue = not self.autoQueue

        
    def __autoDownloader(self):
        #Automatic downloader.
        #Downloads every URL from queue if there is any.
        pass

    def __downloadMenu(self):
        print("Download menu.")
        site_to_download = input("Enter site URL: ")
        print()

        site_downloader.download_site(site_to_download)

    def __parseMenu(self):
        print("Parse menu.")

        #Implement feature to ask user what to do with the dataset
        #user could save dataset to a database or not to save
        #user could also view dataset if wanted

        p = site_parser.Parser()
        return p.create_dataset()


#You could start downloading all the associated URLs related to
#the initial sites URL
#for site in data["links"]:
    #site_downloader.download_site(site)


if __name__ == "__main__":
    WebSurfer()