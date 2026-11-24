import json

class DatasetLoader:
    def __init__(self, f_path):
        self.f_path = f_path
        self.data = []

    def load(self):
        with open(self.f_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        return self.data