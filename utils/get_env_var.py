"""Loads and returns the key from a .env file"""

from dotenv import load_dotenv   #for python-dotenv method
load_dotenv()                    #for python-dotenv method

import os

def get_env_var(var_name: str) -> str:
    return os.environ.get(var_name)

