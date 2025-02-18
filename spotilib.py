import win32gui
import win32api
import time

# Virtual-KeyCodes
Media_Next = 0xB0
Media_Previous = 0xB1
Media_Pause = 0xB3  # Play/Pause
Media_Mute = 0xAD


class SpotifyInterface:
    window_id: int

    def __init__(self, window_id):
        self.window_id = window_id

    def song_info(self):
        try:
            song_info = win32gui.GetWindowText(self.window_id)
        except:
            pass
        return song_info

    def artist(self):
        try:
            temp = self.song_info()
            artist, song = temp.split(" - ", 1)
            artist = artist.strip()
            return artist
        except:
            return "There is noting playing at this moment"

    def song(self):
        try:
            temp = self.song_info()
            artist, song = temp.split(" - ", 1)
            song = song.strip()
            return song
        except:
            return "There is noting playing at this moment"


# Returns SpotifyInterface Obj which should contain the id of the Spotify Window
# To get the id, the user has to have the Spotify Window in the foreground, when this command is executed
# help the user switch to the Spotify Window in time, the command waits 2 seconds per default, before
# the window id of the foreground window is requested
def create_spotify_interface_obj(wait_time=2) -> SpotifyInterface:
    time.sleep(wait_time)
    window_id = win32gui.GetForegroundWindow()
    return SpotifyInterface(window_id)


# Media Controls
def hwcode(Media):
    hwcode = win32api.MapVirtualKey(Media, 0)
    return hwcode


def next():
    win32api.keybd_event(Media_Next, hwcode(Media_Next))


def previous():
    win32api.keybd_event(Media_Previous, hwcode(Media_Previous))


def pause():
    win32api.keybd_event(Media_Pause, hwcode(Media_Pause))


def play():
    win32api.keybd_event(Media_Pause, hwcode(Media_Pause))


def mute():
    win32api.keybd_event(Media_Mute, hwcode(Media_Mute))
