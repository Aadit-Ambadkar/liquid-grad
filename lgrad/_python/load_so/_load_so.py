import urllib.request
from pathlib import Path
import os
import ctypes
import time

def load_so(url):
    (Path.home() / ".lgrad" / "temp/").mkdir(parents=True, exist_ok=True)
    if (not os.path.exists(Path.home() / ".lgrad" / "temp/" / f"compiled_{abs(hash(url)):06x}.so")):
        urllib.request.urlretrieve(url, Path.home() / ".lgrad" / "temp/" / f"compiled_{abs(hash(url)):06x}.so")
    elif (time.time() - os.path.getmtime(Path.home() / ".lgrad" / "temp/" / f"compiled_{abs(hash(url)):06x}.so") > 216000): # 1 day old
        urllib.request.urlretrieve(url, Path.home() / ".lgrad" / "temp/" / f"compiled_{abs(hash(url)):06x}.so")
    return ctypes.CDLL(str(Path.home() / ".lgrad" / "temp/" / f"compiled_{abs(hash(url)):06x}.so"))