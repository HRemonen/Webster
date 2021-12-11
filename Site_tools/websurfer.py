from site_downloader import download_site
import site_downloader
import site_parser

class Instance:
    def __init__(self) -> None:
        pass


def userInterface():
    CHOICES = ["s", "d", "p", "e"]
    choices = """
Choices: 
(s)ettings
(d)ownload site
(p)arse site and create dataset
(e)xit
    """

    print("""Welcome to WebSurfer!
What would you like to do?""")

    while True:
        print(choices)
        c = input("Enter choice: ")
        if c.lower() == "e":
            break
        elif c.lower() not in CHOICES:
            print("Incorrect choice, try again")
        else: 
            try:
                action(c)
            except Exception:
                print("Someting went wrong, try again.")

def action(choice: str):
    if choice == "s":
        print("Settings menu.")

    elif choice == "d":
        print("Download menu.")
        site_to_download = input("Enter site URL: ")
        print()
        site_downloader.download_site(site_to_download)
        
    elif choice == "p":
        print("Parse menu.")

#p = site_parser.Parser()
#data = p.create_dataset()

#You could start downloading all the associated URLs related to
#the initial sites URL
#for site in data["links"]:
    #site_downloader.download_site(site)

#You could also implement db or something else to store
#the downloaded sites.
if __name__ == "__main__":
    userInterface()