"""
This module contains the default settings.

Group similar settings in logical manner.
"""

from os import path

from datetime import datetime

###########################--SETTINGS--###########################

#===================---PATH SETTINGS---===================
TIME_NOW = datetime.now()
PATH = path

#Path to downloads folder
DL_DIR = "downloads/html/"
PARSE_DIR = "downloads/json/"

#==================---CRAWLER SETTINGS---==================
OBEY_ROBOTSTXT = True

#=================---DATABASE SETTINGS---==================
MONGO_URL = ""
MONGO_DB = ""

###########################-/SETTINGS/-###########################