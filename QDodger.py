import keyboard
import sys
from valclient.client import Client
from valclient.exceptions import *

def HandleDodgeErrors():
    try:
        client = Client(region='eu')
        client.activate()
        client.pregame_quit_match()
    except (HandshakeError, ConnectionError, PhaseError) as e:
        print(e)

keyboard.add_hotkey("F6", HandleDodgeErrors)

while True:
    keyboard.wait()
    if keyboard.is_pressed("F7"):
        sys.exit()
        break