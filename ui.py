import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

def create_ui(token, search_for_artist, get_songs_by_artist):
    def search_artist():
        artist_name = entry.get()
        if artist_name: 
            result = search_for_artist(token, artist_name)
            if result:
                artist_id = result["id"]
                songs = get_songs_by_artist(token, artist_id)
                song_names = [song['name'] for song in songs]
                results_text.delete(1.0, tk.END)
                for idx, song in enumerate(songs):
                    song_info = f"{idx + 1}. {song['name']} - Popularity Score: {song['popularity']}"
                    results_text.insert(tk.END, song_info + "\n")
                #messagebox.showinfo("Top Tracks", "\n".join(song_names))
            else:
                results_text.delete(1.0, tk.END)
                results_text.insert(tk.END, "No Artist Found")
                #messagebox.showinfo("No Artist Found", "No artist with this name exists")
        else:
            results_text.delete(1.0, tk.END)
            results_text.insert(tk.END, "Invalid Input")
            #messagebox.showinfo("Invalid Input", "Please enter an artist name")

    window = tk.Tk()
    window.title("Spotify Artist Search")
    window.geometry("800x800")
    window.configure(bg="black")

    window.iconbitmap("./bigounce.ico")

    label = tk.Label(window, text="Enter Artist Name:")
    label.pack()
    label.configure(bg="black")
    label.configure(fg="green")
    entry = tk.Entry(window)
    entry.pack()
    entry.configure(bg="black")
    entry.configure(fg="green")

    def search_button_hover(event):
        search_button.config(bg="#33cc33")

    def search_button_leave(event):
        search_button.config(bg="green")

    search_button = tk.Button(window, text="Search", command=search_artist, font=("Arial", 12, "bold"),
                             bg="green", fg="white", relief="flat", padx=10, pady=5,
                             activebackground="green", activeforeground="white",
                             highlightthickness=0, borderwidth=0)
    
    search_button.pack()
    search_button.bind("<Enter>", search_button_hover)
    search_button.bind("<Leave>", search_button_leave)



    #button = tk.Button(window, text="Search", command=search_artist)
    #button.pack()

    results_text = tk.Text(window, height=10)
    results_text.pack()
    results_text.configure(bg="black")
    results_text.configure(fg="green")

    image_path = "./bigounce.jpg"
    img = Image.open(image_path)
    img = img.resize((400, 400))
    img = ImageTk.PhotoImage(img)
    image_label = tk.Label(window, image=img)
    image_label.pack()

    window.mainloop()
