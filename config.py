import json


class Config:
    def __init__(self):
        self.config = None

    def read_config(self):
        self.config = json.load(open("config.json", "r"))

    def get_base_dir(self) -> str:
        return self.config["base_dir"]

    def get_items(self) -> [object]:
        return self.config["items"]

    def get_labels(self) -> [str]:
        return [item["label"] for item in self.config["items"]]


if __name__ == "__main__":
    config = Config()
    config.read_config()

