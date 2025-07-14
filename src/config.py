from os import path
import secrets

class Config:
    BASE_DIRECTORY = path.abspath(path.dirname(__file__))
    SECRET_KEY = secrets.token_hex(16)
    UPLOAD_PATH = path.join(BASE_DIRECTORY, "static", "upload")
