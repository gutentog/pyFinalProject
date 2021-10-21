#!/usr/bin/env python3
import requests
import os

cwd = os.getcwd()
path = cwd + '/supplier-data/images/'

url = "http://localhost/upload/"

for file in os.listdir(path):
    if not file.startswith('.'):
        if not file.endswith('tiff'):
            full_file_name = path + file
            with open(full_file_name, 'rb') as opened:
                response = requests.post(url, files={'file': opened})
                response.raise_for_status()
                print(response.text)
                print(response.status_code)

# #!/usr/bin/env python3
# import os, sys
# import requests

# url = "http://localhost/upload/"
# path = "supplier-data/images/"

# images = os.listdir(path)

# for image in images:
#   if image.endswith(".jpeg"):
#     with open(path + image, 'rb') as opened:
#       r = requests.post(url, files={'file': opened})
