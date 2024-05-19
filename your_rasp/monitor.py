from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class MyHandler(FileSystemEventHandler):
    def __init__(self, process):
        self.process = process
        
    def on_modified(self, event):
        print("File modified. Restarting server...")
        self.process.terminate()
        self.process.wait()
        self.process = subprocess.Popen(["python", "server.py"])
        

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    process = observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
      
    observer.join()
