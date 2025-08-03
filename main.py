from tkinter import *
from PIL import Image, ImageTk
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
from tkinter import messagebox
load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = os.getenv("MY_VERIFIED_NUMBER")

BACKGROUND_COLOR = "#B1DDC6"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
IMAGE_MAX_WIDTH = 300
IMAGE_MAX_HEIGHT = 300


window = Tk()
window.title("🎵 Lyrics Finder 🎵")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)
window_label=Label(text="🎵 Lyrics Finder 🎵",bg=BACKGROUND_COLOR, font=("Courier", 20, "bold"))
window_label.grid(row=0, column=1,padx=150, sticky="w")
original_img = Image.open(r"D:\python\My codeeess\date and time\API\Lyrics_finder\transparent_logo.png")

original_img.thumbnail((IMAGE_MAX_WIDTH, IMAGE_MAX_HEIGHT))

logo_img = ImageTk.PhotoImage(original_img)

canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(WINDOW_WIDTH//2, 100, image=logo_img, anchor="n")
canvas.grid(row=1, column=1)

song_label=Label(text="Song Title", bg=BACKGROUND_COLOR, font=("Courier", 14, "bold"))
song_label.grid(row=2, column=0, pady=10, sticky="w")

artist_label=Label(text="Artist Name", bg=BACKGROUND_COLOR, font=("Courier", 14, "bold"))
artist_label.grid(row=3, column=0, pady=10, sticky="w")

song_entry=Entry(width=35)
song_entry.focus()
song_entry.grid(row=2, column=1, columnspan=2, sticky="w")

artist_entry=Entry(width=35)
artist_entry.grid(row=3, column=1, columnspan=2, sticky="w")

status_label = Label(text="", bg=BACKGROUND_COLOR, font=("Courier", 12, "bold"), fg="green")
status_label.grid(row=5, column=1, columnspan=2, sticky="w")

def search():
    song_title = song_entry.get()
    artist = artist_entry.get()
    
    base_url = "https://api.genius.com/search"
    headers = {
        "Authorization": f"Bearer {os.getenv('GENIUS_ACCESS_TOKEN')}"

    }
    params = {"q": f"{song_title} {artist}"}
    
    response = requests.get(base_url, headers=headers, params=params)
    data = response.json()
    
    if data["response"]["hits"]:
        song_info = data["response"]["hits"][0]["result"]
        title = song_info["title"]
        url = song_info["url"]
        print(f"Found: {title}\nURL: {url}")
        status_label.config(text=f"Lyrics URL found! Open browser:\n{url}", fg="green")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Lyrics for '{title}': {url}",
            from_=from_number,
            to=to_number
        )
        print("Message SID:", message.sid)
        messagebox.showinfo("Success", "Lyrics link sent via SMS!")
    else:
        print("No results found.")
        status_label.config(text="No results found.", fg="red")
        messagebox.showwarning("Not Found", "No results found to send.")
lyrics_button=Button(text="Get Lyrics",bg="#4CAF50", fg="white",width=20,command=search)
lyrics_button.grid(row=4,column=1,columnspan=2, sticky="w")
window.mainloop()
