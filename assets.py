import pygame
import os
import json
from cryptography.fernet import Fernet

# function for key
def get_key(key_file=None):
    if key_file is None:
        appdata = os.getenv('APPDATA')
        key_file = os.path.join(appdata, "Clicker", "key.key")

    key_dir = os.path.dirname(key_file)
    if not os.path.exists(key_dir):
        os.makedirs(key_dir, exist_ok=True)

    if not os.path.exists(key_file):
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
        return key
    with open(key_file, "rb") as f:
        return f.read()

# folder for config
def folder():
    os.makedirs("data/configs", exist_ok=True)

    key = get_key()  # using keys
    fernet = Fernet(key)

    # dumping
    config_data = json.dumps({'score': 0}).encode("utf-8")
    config = fernet.encrypt(config_data)

    config_path = "data/configs/main_config.json"
    if not os.path.exists(config_path):
        with open(config_path, "wb") as file_write:
            file_write.write(config)

# loading assets
def load_assets():
    pygame.init()
    pygame.mixer.init(44100, -16, 1, 512)

    folder()

    key = get_key()
    fernet = Fernet(key)

    # reading config
    with open("data/configs/main_config.json", "rb") as file_read:
        enc_data = file_read.read()
        decoded_data = fernet.decrypt(enc_data)
        data = json.loads(decoded_data.decode("utf-8"))

    # loading assets
    font = pygame.font.Font("data/font/Pixel.ttf", 23)
    font_1 = pygame.font.Font("data/font/Pixel.ttf", 13)

    click_ico = pygame.image.load("data/png/click(1).ico")
    click_me = pygame.image.load("data/png/Click_me.png")
    click_sound = pygame.mixer.Sound("data/sounds/Click.mp3")

    return {
        "score": data["score"],
        "ico": click_ico,
        "click_me": click_me,
        "font": font,
        "font_1": font_1,
        "click_sound": click_sound,
    }
def save_score(score):
    key = get_key()
    fernet = Fernet(key)

    config_data = json.dumps({"score": score}).encode("utf-8")
    config = fernet.encrypt(config_data)

    config_path = "data/configs/main_config.json"
    with open (config_path, "wb") as file_write:
        file_write.write(config)
