import os
import time
import subprocess

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Pug(FileSystemEventHandler):
    def on_modified(self, event):
        print('build')
        subprocess.run(['npm', 'run', 'build'])


def bark():
    event_handler = Pug()
    observer = Observer()
    observer.schedule(event_handler, './src')
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    bark()
