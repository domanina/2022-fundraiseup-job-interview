import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

HEADLESS_MODE = os.environ.get("HEADLESS_MODE")
RUN_BROWSER = os.environ.get("RUN_BROWSER")
