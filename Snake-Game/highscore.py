import os

FILE = "highscore.txt"

def load_highscore():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return int(f.read())
    return 0

def save_highscore(score):
    with open(FILE, "w") as f:
        f.write(str(score))