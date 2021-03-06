

import pafy, sys
from subprocess import Popen, TimeoutExpired, PIPE
import configurations
from speech.listener import Listener

SupportedExtensions = ["m4a", "ogg"]


class AudioPlayer:

  song = None

  def __init__(self, song):
    self.song = song

  def play(self, song=None):
    if song is None:
      print("Playing " + self.song.title + " by " + self.song.artist)
      self._play_song(self._get_song())
    else:
      print("Playing " + song.title + " by " + self.song.artist)
      self._play_song(self._get_song(song))

  def _play_song(self, obj):
    stream = obj.getbestaudio()
    stream.download(filepath=configurations.BUFFERED_TEMP_LOCATION+"."+stream.extension)
    self._play_audio(stream.extension)

  def _play_audio(self, ext):
    if ext not in SupportedExtensions:
      sys.stderr.write("Extension " + ext + " not in supported extensions\n")

    self._play(ext)

  def _play(self, ext):

    mplayer = Popen(["mplayer", "-slave", "-really-quiet", configurations.BUFFERED_TEMP_LOCATION+"."+ext], stdin=PIPE)
    listener = Listener()
    paused = False
    stdin = mplayer.stdin
    while mplayer.poll() is None:
        if not paused:
          command = listener.get_input("Break/Stop", False, timeout=configurations.COMMAND_TIMEOUT)
        else:
          command = listener.get_input("Play/Stop", False, timeout=configurations.COMMAND_TIMEOUT)
        if command is not None:
          command = command.lower()
          if command == "break" and not paused: 
            stdin.write(b"p\n")
            stdin.flush()
            paused = True
          elif command == "play" and paused:
            stdin.write(b"p\n")
            stdin.flush()
            paused = False
          elif command == "stop":
            mplayer.terminate()
            break
          elif command == "volume up":
            stdin.write(b"/\n")
            stdin.flush()
          elif command == "volume down":
            stdin.write(b"*\n")
            stdin.flush()


  def _get_song(self, song=None):
    if song is None:
      return pafy.new(self.song.url)
    else:
      return pafy.new(song.url)

