import urllib.request
from pathlib import Path
import os
import ctypes

def load_so(url):
    Path("~/.lgrad/temp/").mkdir(parents=True, exist_ok=True)
    if (not os.path.exists(f"~/.lgrad/temp/compiled_{abs(hash(url)):06x}.so")):
        urllib.request.urlretrieve(url, f"~/.lgrad/temp/compiled_{abs(hash(url)):06x}.so")
    # elif (os.path.getmtime(f"~/.lgrad/temp/compiled_{abs(hash(url)):06x}.so"))
    return ctypes.CDLL(f'~/.lgrad/temp/compiled_{abs(hash(url)):06x}.so')