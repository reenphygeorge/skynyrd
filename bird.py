import time
from datetime import datetime
import pyglet

# Set the desired time and date
target_time = datetime.strptime("23:55:05", "%H:%M:%S").time().strftime("%H:%M:%S")
target_date = datetime.strptime("12-31", "%m-%d").date()

# Specify the audio file path
audio_file_path = "Free-Bird.wav"  # Replace with your file path

if datetime.now().date().strftime("%m-%d") == target_date.strftime("%m-%d"):
    # Calculate the initial sleep time to align with the target time
    current_time = datetime.now().time().strftime("%H:%M:%S")
    time_difference = datetime.strptime(target_time, "%H:%M:%S") - datetime.strptime(current_time, "%H:%M:%S")
    initial_sleep = max(time_difference.total_seconds(), 0)

    # Sleep initially
    time.sleep(initial_sleep)

    # Play the audio using pyglet
    sound = pyglet.media.load(audio_file_path, streaming=False)
    sound.play()

    # Keep the program running until the audio finishes playing
    pyglet.app.run()
else:
    print("It's not New Year's Eve!")