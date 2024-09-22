import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Don't you see me I", 0.21),
        ("I think i'm falling, i'm falling for you", 0.1),
        ("And don't you need me I", 0.21),
        ("I think i'm falling, i'm falling for you", 0.15),
        ("On this night, and in this light", 0.18),
        ("I think i'm falling, i'm falling for you", 0.13),
        ("And maybe you, change your mindddddddd", 0.1),
    ]
    delays = [0.22, 5.0, 11.0, 16.0, 22.1, 25.5, 27.8, 33.2, 39.3]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()