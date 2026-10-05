import os
from flask import Flask, render_template

app = Flask(__name__)

GROUP_INFO = {
    "name": "HOTBOX RECORDS",
    "tagline": "Melodies. Hard Lyrics. Real Stories.",
    "bio": "Formed in 2022, Hotbox Records brings new waves and heavy-hitting trap beats and melodies from the underground straight to the world.",
    "socials": {
        "youtube": "https://www.youtube.com/@HotBoxRecords1920",
        "instagram": "https://www.instagram.com/hotboxrecords1920/"
    },
    "members": [
        {
            "stage_name": "Tyler Charles",
            "role": "Artist / Lyricist",
            "bio": "Crafts sharp verses and reflective flows.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=Tyler+Charles"
        },
        {
            "stage_name": "WAL",
            "role": "Artist / Lyricist",
            "bio": "Delivers heavy punchlines and relentless cadence.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=WAL"
        },
        {
            "stage_name": "EMENEL",
            "role": "Artist / Lyricist",
            "bio": "Known for versatile delivery and high-energy hooks.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=EMENEL"
        },
        {
            "stage_name": "Psalm D",
            "role": "Artist / Lyricist",
            "bio": "Brings intricate rhyming patterns and deep storytelling.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=Psalm+D"
        },
        {
            "stage_name": "Daniel",
            "role": "Artist / Lyricist",
            "bio": "Combines smooth cadences with heavy lyrical presence.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=Daniel"
        },
        {
            "stage_name": "Yusha",
            "role": "Artist / Lyricist",
            "bio": "Adds dark melodic contrast and signature choruses.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=Yusha"
        },
        {
            "stage_name": "Don Co",
            "role": "Sound Engineer",
            "bio": "Mastermind behind the crisp mix, low-end balance, and final audio master.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=Don+Co"
        },
        {
            "stage_name": "JA",
            "role": "Artist / Lyricist",
            "bio": "Brings fast-paced flows and sharp hook construction.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=JA"
        },
        {
            "stage_name": "Krux",
            "role": "Artist / Lyricist",
            "bio": "Delivers gritty bars and relentless rhythm across beats.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=Krux"
        },
        {
            "stage_name": "OG Huslah",
            "role": "Artist / Lyricist",
            "bio": "Brings raw street poetry, heavy cadence, and veteran status.",
            "image": "https://via.placeholder.com/300x300/111111/00ff88?text=OG+Huslah"
        }
    ],
    "tracks": [
        {
            "title": "SIMULA",
            "artist": "EMENEL ft. Tyler Charles, Daniel, Psalm D",
            "url": "https://youtu.be/3KHt4r3KBoA"
        },
        {
            "title": "Parang Abo Lang",
            "artist": "Daniel",
            "url": "https://www.youtube.com/watch?v=gXpk2m0XEys"
        },
        {
            "title": "Laging Ikaw",
            "artist": "Tyler Charles",
            "url": "https://youtu.be/pdffbaSoW0c"
        },
        {
            "title": "Hustle Without Hassle",
            "artist": "Huslah x Yusha",
            "url": "https://youtu.be/qMBWu1q4xHA"
        },
        {
            "title": "Saan?",
            "artist": "JA",
            "url": "https://youtu.be/kDjQWVTk__8"
        },
        {
            "title": "Eternal Love",
            "artist": "Don Co",
            "url": "https://youtu.be/esPWprCVOmw?si=PaspUFIv-L8OLoRv"
        },
        {
            "title": "BEYOND THE BLOCK",
            "artist": "WAL ft. Petsanity",
            "url": "https://youtu.be/Jrde2GeLJ48"
        }
    ]
}

@app.route("/")
def home():
    return render_template("index.html", group=GROUP_INFO)
   if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
