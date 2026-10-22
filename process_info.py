import os

processes = {}

for entry in os.listdir("/proc"):
    if entry.isdigit():
        pid = entry

        try:
            with open(f"/proc/{pid}/status") as file:
                name = ""
                ppid = ""

                for line in file:
                    if line.startswith("Name:"):
                        name = line.split(":")[1].strip()

                    elif line.startswith("PPid:"):
                        ppid = line.split(":")[1].strip()

                processes[pid] = {
                    "name": name,
                    "ppid": ppid
                }

        except FileNotFoundError:
            pass

for pid, info in processes.items():
    print(
        f"PID: {pid} "
        f"PPID: {info['ppid']} "
        f"Name: {info['name']}"
    )
