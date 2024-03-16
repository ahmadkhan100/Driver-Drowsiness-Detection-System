# alert_system.py
import os
from pygame import mixer  # Used to play sound

# Initialize the mixer module
mixer.init()

def play_sound(sound_file):
    """Play sound from the given sound file."""
    mixer.music.load(sound_file)
    mixer.music.play()

def drowsiness_alert():
    """Play a drowsiness alert sound."""
    alert_sound = 'alert.wav'  # Replace with the path to your alert sound file
    play_sound(alert_sound)

# If you have a more complex alert system, you could add more functions here



