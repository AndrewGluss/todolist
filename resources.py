import os
import json


def print_with_indent(value, indent=0):
    indentation = '\t' * indent
    print(indentation + str(value))


class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for i in self.entries:
            i.print_entries(indent + 1)

    def json(self):
        res = {
            "title": self.title,
            "entries": [entry.json() for entry in self.entries]
        }
        return res

    @classmethod
    def from_json(cls, value):
        e = cls(value['title'])
        for v in value.get('entries', []):
            e.add_entry(cls.from_json(v))
        return e

    def save(self, path):
        x = os.path.join(path, self.title)
        with open(f"{x}.json", "w", encoding="utf-8") as f:
            json.dump(self.json(), f)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            res = json.load(f)
        return cls.from_json(res)


category = Entry('Еда')

category.add_entry(Entry('Морковь'))
category.add_entry(Entry('Капуста'))

