import os
import random
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


class MusicMixer:
    def __init__(self, master):
        self.master = master
        master.title("Music Mixer")
        master.geometry("400x300")

        self.source_label = tk.Label(master, text="Source Folder:")
        self.source_label.pack()

        self.source_button = tk.Button(master, text="Choose Folder", command=self.choose_source)
        self.source_button.pack()

        self.dest_label = tk.Label(master, text="Destination Folder:")
        self.dest_label.pack()

        self.dest_button = tk.Button(master, text="Choose Folder", command=self.choose_dest)
        self.dest_button.pack()

        self.mix_button = tk.Button(master, text="Mix Music", command=self.mix_music)
        self.mix_button.pack()

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack()

    def choose_source(self):
        self.source_path = filedialog.askdirectory()
        self.source_label.configure(text="Source Folder: " + self.source_path)

    def choose_dest(self):
        self.dest_path = filedialog.askdirectory()
        self.dest_label.configure(text="Destination Folder: " + self.dest_path)

    def mix_music(self):
        if not hasattr(self, 'source_path') or not hasattr(self, 'dest_path'):
            messagebox.showerror("Error", "Please select both source and destination folders.")
            return

        music_files = []
        for file in os.listdir(self.source_path):
            if file.endswith('.mp3') or file.endswith('.wav'):
                music_files.append(file)

        if len(music_files) == 0:
            messagebox.showwarning("Warning", "No music files found in source folder.")
            return

        random.shuffle(music_files)

        for file in music_files:
            source_file_path = os.path.join(self.source_path, file)
            dest_file_path = os.path.join(self.dest_path, file)
            shutil.copy2(source_file_path, dest_file_path)

        messagebox.showinfo("Success", "Music mixing completed.")


if __name__ == '__main__':
    root = tk.Tk()
    app = MusicMixer(root)
    root.mainloop()