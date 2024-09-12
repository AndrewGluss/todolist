from resources import Entry
from typing import List
import os


class EntryManager:
    def __init__(self, data_path):
        self.data_path: str = data_path
        self.entries: List[Entry] = []

    def save(self):
        for i in self.entries:
            i.save(self.data_path)

    def load(self):
        for item in os.listdir(self.data_path):
            if os.path.isdir(item) == False:
                if item[-5:] == '.json':
                    e = Entry.load(os.path.join(self.data_path, item))
                    self.entries.append(e)

    def add_entry(self, title):
        e = Entry(title)
        self.entries.append(e)