import json


class Config:
    def __init__(self):
        self.config = None
        self.labels = None
        self.items = None

    def read_config(self):
        self.config = json.load(open("config.json", "r"))
        self.items = self.config["items"]
        self.labels = [item["label"] for item in self.items]

    def get_base_dir(self) -> str:
        return self.config["base_dir"]

    def get_items(self) -> [object]:
        return self.items

    def get_labels(self) -> [str]:
        return self.labels

    def is_binary(self, label) -> bool:
        for item in self.items:
            if item["label"] == label:
                return item["is_binary"]


if __name__ == "__main__":
    config = Config()
    config.read_config()

