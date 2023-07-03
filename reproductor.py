import tkinter as tk
from pygame import mixer
from funciones import play_audio
from funciones import pause_audio
from funciones import resume_audio
from funciones import stop_audio
from funciones import increase_volume
from funciones import decrease_volume
from funciones import next_song
from funciones import previous_song

mixer.init()
window = tk.Tk()
window.rowconfigure(2, minsize=50, weight=1)
window.columnconfigure(2, minsize=50, weight=1)

lbl_song_name = tk.Label(master=window, text="Song Name")

btn_play = tk.Button(master=window, text="Play", command=play_audio)
btn_pause = tk.Button(master=window, text="Pause", command=pause_audio)
btn_stop = tk.Button(master=window, text="Stop", command=stop_audio)
btn_resume = tk.Button(master=window, text="Resume", command=resume_audio)
btn_increaseVolume = tk.Button(master=window, text="+", command=increase_volume)
btn_decreaseVolume = tk.Button(master=window, text="-", command=decrease_volume)
btn_next = tk.Button(master=window, text="Next", command=next_song)
btn_previous = tk.Button(master=window, text="Previous", command=previous_song)

lbl_song_name.grid(row=0, column=0, columnspan=4)

button_width = 10
button_height = 3
btn_play.config(width=button_width, height=button_height)
btn_pause.config(width=button_width, height=button_height)
btn_resume.config(width=button_width, height=button_height)
btn_stop.config(width=button_width, height=button_height)
btn_increaseVolume.config(width=button_width, height=button_height)
btn_decreaseVolume.config(width=button_width, height=button_height)
btn_next.config(width=button_width, height=button_height)
btn_previous.config(width=button_width, height=button_height)



btn_stop.grid(row=2, column=1, sticky="nsew", columnspan=1)
btn_pause.grid(row=2, column=0, sticky="nsew", columnspan=1)
btn_resume.grid(row=2, column=2, sticky="nsew", columnspan=1)
btn_play.grid(row=1, column=1, sticky="nsew", columnspan=1)
btn_increaseVolume.grid(row=1, column=2, sticky="nsew", columnspan=1)
btn_decreaseVolume.grid(row=1, column=0, sticky="nsew", columnspan=1)
btn_next.grid(row=1, column=3, sticky="nsew", columnspan=1)
btn_previous.grid(row=2, column=3, sticky="nsew", columnspan=1)

window.title("VarpuAmp")
window.grid_rowconfigure(0, minsize=200)
window.grid_columnconfigure(1, minsize=200)
window.mainloop()