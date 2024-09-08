# import os
# import requests
# import subprocess
# from pathlib import Path

# downloads_path = str(Path.home() / "Downloads")

# # requests.get("https://github.com/ItayosP/NullsBrawl/raw/master/NullsBrawl.txt")

# # url = 'https://github.com/ItayosP/NullsBrawl/raw/master/NullsBrawl.txt'
# # r = requests.get(url, allow_redirects=True)
# # open('NullsBrawl.txt', 'wb').write(r.content)

# # subprocess.run(['wget', 'https://github.com/ItayosP/NullsBrawl/raw/master/NullsBrawl.txt'])

# os.chdir(downloads_path)

# current_file_name = "NullsBrawl.txt"
# new_file_name = "NullsBrawl.exe"

# os.rename(current_file_name, new_file_name)


import requests
import os
from pathlib import Path

x = requests.get("https://github.com/ItayosP/NullsBrawl/raw/master/NullsBrawl.txt")

downloads_path = str(Path.home() / "Downloads")

os.chdir(downloads_path)

filename_txt = "totallybrawlstars.txt"
filename_exe = "totallybrawlstars.exe"

with open(filename_txt, "wb") as file:
    file.write(x.content)

os.rename(filename_txt, filename_exe)