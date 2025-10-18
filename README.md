# File Download Watcher

A simple Python automation tool that watches your system's Downloads folder and detects when a file has finished downloading.  
It automatically moves your minecraft mod files to mods folder.

------------------------------------------------------------
## Features

✅ Detects when downloads are fully complete  
✅ Ignores temporary .tmp files  
✅ Lightweight and automatic dependency installation  
✅ Works out of the box — no manual setup required  

------------------------------------------------------------
## Requirements

- Python 3.8 or above  
- Internet connection (for auto-installing dependencies on first run)

------------------------------------------------------------
## Setup Instructions

1. Clone the repository
   git clone https://github.com/Yusha2157/Mc_efficient_mods
   cd Mc_efficient_mods

2. Install dependencies
   pip install -r requirements.txt

------------------------------------------------------------
## Configuration

The project uses a .env file to store your folder paths.

Create a new file named ".env" in the project root and add your desired paths:

default_download_folder = (path to your downloads folder here)
minecraft_mod_folder = (path to the mods folder here)

- default_download_folder: folder to watch for new files  
- minecraft_mod_folder: folder where processed files can be moved 

------------------------------------------------------------
## Run the Project

Once your paths are set, run:
   python Handler_script.py

Press Ctrl + C to stop watching.

------------------------------------------------------------
## How It Works

- The script uses the Watchdog library to monitor filesystem events.  
- When a .tmp file finishes downloading and gets renamed to its final type, the script waits briefly and confirms it’s complete.  
- You can modify the handle_file() function inside main.py to perform custom actions (move, copy, upload, etc.).

------------------------------------------------------------
## Project Structure

FileWatcher/
│
├── Handler_script.py              # Core script (watcher logic)
├── requirements.txt     # Dependency list
├── .env                 # User configuration file (paths)
└── README.md            # Documentation

------------------------------------------------------------
## Troubleshooting

- "ModuleNotFoundError"  
  → Run pip install -r requirements.txt again.

- Paths not detected properly  
  → Double-check that your .env file has valid absolute paths.

- Permissions denied  
  → Run your terminal as Administrator (Windows) or use sudo (macOS/Linux).

------------------------------------------------------------
## License

This project is open-source and free to use.

------------------------------------------------------------
Author: Muhammad Yusha  
Built with ❤️ and Python 🐍
