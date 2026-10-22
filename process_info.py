import os

for entry in os.listdir("/proc"):
    if entry.isdigit():
        print(entry)
