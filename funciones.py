from pygame import mixer
import pygame
import os

path_song = r"C:\Users\villa\OneDrive\Escritorio\Matias\Varpu-amp\Ziggy Stardust and the Spiders from Mars"

songs = [file for file in os.listdir(path_song)]


current_song_index = 0

def play_audio():
    pygame.mixer.music.load(os.path.join(path_song, songs[current_song_index]))
    mixer.music.play()
    
def pause_audio():
    mixer.music.pause() 

def resume_audio():
    mixer.music.unpause()

def stop_audio():
    mixer.music.stop()

def increase_volume():
    current_volume = mixer.music.get_volume()
    new_volume = min(current_volume + 0.1, 1.0)  # Increase the volume by 0.1 (maximum 1.0)
    mixer.music.set_volume(new_volume)

def decrease_volume():
    current_volume = mixer.music.get_volume()
    new_volume = max(current_volume - 0.1, 0.0)  # Decrease the volume by 0.1 (minimum 0.0)
    mixer.music.set_volume(new_volume)
    
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_audio()

def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_audio()