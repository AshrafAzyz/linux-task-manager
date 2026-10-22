import os

pid = os.getpid()

print("My PID:", pid)

with open(f"/proc/{pid}/status") as file:
    for line in file:
        print(line, end="")
