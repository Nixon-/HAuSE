
ARGS = dict()

class DB():
  NAME = "HAuSE"
  
  class COLLECTIONS():
    COMMANDS = "COMMANDS"
    MUSIC = "MUSIC"
    NOTES = "NOTES"
  
COMMAND_CACHE_SIZE = 10

BUFFERED_TEMP_FILE_PATH = "/tmp/"
BUFFERED_TEMP_FILE_PREFIX = "HAuSE-temp"
BUFFERED_TEMP_LOCATION = BUFFERED_TEMP_FILE_PATH + BUFFERED_TEMP_FILE_PREFIX
BUFFERED_TEMP_FILES = 10

FACEBOOK_APP_ID = 751834808279364
FACEBOOK_APP_SECRET = "e188187db9b470a1c885a7fef8ef9fad"

TWITTER_APP_KEY = "4Lqt3vKytFl6wJqJkZsYZpqJF" 
TWITTER_APP_SECRET = "5gisfb7qH2NNAVBPG2dc3bHnSZSLk2LDhsSxjt03Y5J4SSnexI"
TWITTER_OAUTH_KEY = "2904896653-8wxkL21seGnpOCmsoRU3nhZZRAnS4wN2sQcFS3W" 
TWITTER_OAUTH_SECRET = "wS7g8l5IK5FmdNAgBvq2SnP69UzGMnUJKKECh9q6J75vs"

def parseArgs(argv):
  global ARGS
  ARGS = dict()
  ARGS["quiet"] = False
  for arg in argv:
    if arg == "--quietMode":
      ARGS["quiet"] = True


