from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
PASSWORD = os.getenv("PASSWORD")
INVENTORY_API = os.getenv("INVENTORY_API") 