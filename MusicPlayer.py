import os
from tkinter import *
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog
from pygame import mixer



class MusicPlayer(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title("Music Player")
        self.geometry("555x315")
        

        # Create a listbox to display the songs
        self.songs_listbox = tk.Listbox(self,selectmode=SINGLE, bg="pink",fg="purple",font=('arial',15),height=12,width=47, background="pink", foreground="purple")
        self.songs_listbox.pack(side="top", fill="both", expand=True)

        # Create a self to display the current song
        self.current_song_label= tk.Label(self)
        self.current_song_label.pack()

        #font is defined which is to be used for the button font
        defined_font = font.Font(family='Helvetica')

        top = tk.Listbox(self,bg="purple")
        top.pack(padx=10,pady=5, anchor='center')
        
        # Create a button to add songs to the listbox
        self.add_songs_button = tk.Button(self, text="Add Songs",command=self.add_songs)
        self.add_songs_button.pack(pady=15,in_=top, side='left')

        # Create a button to previous the current song
        self.prev_song_button = tk.Button(self, text="Prev",command=self.prev_song)
        self.prev_song_button.pack(pady=15,in_=top, side='left')

        # Create a button to play the current song
        self.play_button = tk.Button(self, text="Play",command=self.play)
        self.play_button.pack(pady=15,in_=top, side='left')

        # Create a button to pause the current song
        self.pause_button = tk.Button(self, text="Pause", command=self.pause)
        self.pause_button.pack(pady=15,in_=top, side='left')

        # Create a button to unpause the current song
        self.unpause_button = tk.Button(self, text="Resume", command=self.unpause)
        self.unpause_button.pack(pady=15,in_=top, side='left')

        # Create a button to next the current song
        self.next_song_button = tk.Button(self, text="Next", command=self.next_song)
        self.next_song_button.pack(pady=15,in_=top, side='left')

        # Create a button to stop the current song
        self.stop_button = tk.Button(self, text="Stop", command=self.stop)
        self.stop_button.pack(pady=15,in_=top, side='left')


        # Initialize the mixer module
        mixer.init()

    def add_songs(self):
        # Get the songs from the user
        songs = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])

        # Add the songs to the listbox
        for song in songs:
            self.songs_listbox.insert("end", song)

    def prev_song(self):
        # Previous the current song
        current_song = self.songs_listbox.get(ACTIVE)
        print(current_song[0:4])
        
        prev_one = self.songs_listbox.curselection()
        prev_one =-1
        
        mixer.music.load(self.songs_listbox.get(ACTIVE))
        mixer.music.play()

        self.songs_listbox.selection_clear(0,END)
        self.songs_listbox.activate(prev_one)
        self.songs_listbox.selection_set(prev_one)

    def play(self):
        # Get the current song from the listbox
        current_song = self.songs_listbox.get(ACTIVE)
        print(current_song[0:-4])
        # Play the current song
        mixer.music.load(self.songs_listbox.get(ACTIVE))
        mixer.music.play()

    def pause(self):
        # Pause the current song
        mixer.music.pause()

    def unpause(self):
        # Unpause the current song
        mixer.music.unpause()

    def next_song(self):
        # Next the current song
        current_song = self.songs_listbox.get(ACTIVE)
        print(current_song[0:4])

        next_one = self.songs_listbox.curselection()
        next_one =+1
        
        mixer.music.load(self.songs_listbox.get(ACTIVE))
        mixer.music.play()

        self.songs_listbox.selection_clear(0,'end')
        self.songs_listbox.activate(next_one)
        self.songs_listbox.selection_set(next_one)
    def stop(self):
        # Stop the current song
        mixer.music.stop()

    

if __name__ == "__main__":
    music_player = MusicPlayer()
    music_player.mainloop()

