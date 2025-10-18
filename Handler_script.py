from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv
import time , os
import shutil

load_dotenv()

class NewFileHandler(FileSystemEventHandler):
    files_handled = 1
    def __init__(self):
        self.seen = set()

    def handle_file(self, path):
        if path in self.seen:
            return
        self.seen.add(path)

        if path.endswith((".tmp" , ".crdownload")):
            return
        
        time.sleep(2)
        try:
            if os.path.exists(path):
                if path.lower().endswith(".jar"):
                    source = path
                    base_name = os.path.basename(source)
                    move_to = os.getenv("minecraft_mod_folder")
                    destination = os.path.join(move_to , base_name)
                    shutil.move(source , destination)
                    print(f"Successfuly Moved {NewFileHandler.files_handled} files.")
                    NewFileHandler.files_handled += 1
        except Exception as e:
            pass
    
    def on_created(self , event):
        if not event.is_directory:
            self.handle_file(event.src_path)
    
    def on_moved(self, event):
        if not event.is_directory:
            self.handle_file(event.dest_path)
        
if __name__ == "__main__":
    path = os.getenv("default_download_folder")
    file_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(file_handler , path , recursive=False)
    observer.start()

    print(f"Watching for new minecraft mod files inside downloads")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped watching.")
    observer.join()