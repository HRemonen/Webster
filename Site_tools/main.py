import site_downloader
import site_parser


# This is for the manual initial download
site_to_download="" #Enter site to download
s1 = site_downloader.download_site(site_to_download)

p = site_parser.Parser()
data = p.create_dataset()

#You could start downloading all the associated URLs related to
#the initial sites URL
for site in data["links"]:
    site_downloader.download_site(site)

#You could also implement db or something else to store
#the downloaded sites.