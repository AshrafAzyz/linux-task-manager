# Linux Task Manager

A Linux system-monitoring application built with Python and PySide6.

The goal of this project is to understand how Linux manages processes and exposes system information through the `/proc` filesystem, while gradually building a graphical task manager.

## Project Goals

This project is designed to learn:

- Linux process architecture
- Process IDs (PID)
- Parent Process IDs (PPID)
- The Linux `/proc` filesystem
- Process discovery
- Process hierarchy
- CPU and memory monitoring
- Linux signals
- GUI development with PySide6
- Real-time system monitoring

## Architecture

```text
Linux Task Manager
        │
        ▼
   Python GUI
        │
   ┌────┴─────┐
   │          │
Process    System
Manager    Monitor
   │          │
   ▼          ▼
 /proc/PID   /proc/stat
 /proc/PID   /proc/meminfo
   │
   ▼
Linux Kernel
   │
   ▼
Hardware
```

## Current Progress

### Process Information

The project currently reads process information directly from Linux's `/proc` filesystem.

For each process, we can retrieve:

- PID — Process ID
- PPID — Parent Process ID
- Name — Process name

Example:

```text
PID: 1234  PPID: 1000  Name: bash
PID: 1250  PPID: 1234  Name: python
```

### Process Discovery

Linux exposes running processes as directories inside:

```text
/proc
```

For example:

```text
/proc/1
/proc/100
/proc/500
/proc/1234
```

Directories whose names consist only of numbers represent process IDs.

The project discovers these processes using Python:

```python
for entry in os.listdir("/proc"):
    if entry.isdigit():
        pid = entry
```

### Process Status

Detailed information about a process can be found in:

```text
/proc/<PID>/status
```

For example:

```text
/proc/1234/status
```

The project currently reads the `Name` and `PPid` fields from this file.

## Why `/proc`?

`/proc` is a virtual filesystem provided by the Linux kernel.

It does not behave like a normal directory containing files stored permanently on disk.

Instead, Linux exposes information about the running system through it.

For example:

```text
/proc/1/status
```

represents information about process `1`.

This allows the application to communicate with the operating system using normal file operations such as:

```python
open()
read()
```

## Project Structure

Current structure:

```text
linux-task-manager/
│
├── .git/
├── .gitignore
├── .venv/
│
└── process_info.py
```

The project will be expanded as more components are implemented.

## Planned Features

- [x] Discover running processes
- [x] Read process names
- [x] Read parent process IDs
- [x] Store process information
- [x] Group processes by parent
- [ ] Build process tree
- [ ] Create Process class
- [ ] Calculate CPU usage
- [ ] Calculate memory usage
- [ ] Display processes in GUI
- [ ] Real-time process updates
- [ ] Process selection
- [ ] Send process signals
- [ ] Disk monitoring
- [ ] Network monitoring
- [ ] System information
- [ ] PySide6 graphical interface

## Technologies

- Python
- PySide6
- Linux
- `/proc` filesystem
- Git
- GitHub

## Learning Focus

This project is not intended to simply reproduce an existing task manager.

The main objective is to understand the relationship between:

```text
Application
    ↓
Python
    ↓
/proc
    ↓
Linux Kernel
    ↓
Hardware
```

By building the application from the Linux interfaces upward, the project provides practical experience with Linux system programming concepts.

## Author

**Ahmad Ashraf Bin Abdul Aziz**

Computer Engineering  
Universiti Teknologi PETRONAS

GitHub: `AshrafAzyz`
