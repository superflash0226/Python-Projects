import datetime
now = datetime.datetime.now()
timestamp_str = now.strftime("\n %d/%m/%Y \n %H:%M:%S\n")
print(f" TimeStamp {timestamp_str}")

import requests
import re

url = "Enter the link of the website"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

with open("file_name.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("HTML page saved successfully as contact_us.html")

with open("file_name.html", "r", encoding="utf-8") as f:
    content = f.read()

link_pattern = r"https?://[^\s\"'>]+"

links = re.findall(link_pattern, content)

link_unique = set(links)

with open("file_name_output.txt", "w", encoding="utf-8") as f:

    f.write("Link Pattern Used:\n")
    f.write(link_pattern + "\n\n")

    if link_unique:
        f.write("Links Found:\n")
        for link in link_unique:
            f.write(link + "\n")
    else:
        f.write("No links found on this webpage.\n")

print("Links saved successfully in contact_us_output.txt")