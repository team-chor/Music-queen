# Powered By Team riteshcoder
from RiteshMusic import Anony
from RiteshMusic.core.dir import dirr
from RiteshMusic.core.git import git
from RiteshMusic.core.userbot import Userbot
from RiteshMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
