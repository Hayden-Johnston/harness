import json
from providers.openai_client import OpenAI_Client
from config.storage_manager import Storage
from config.command_registry import CommandRegistry

class Config:

    def __init__(self):
        self.config = self.get_config()
        self.endpoints = self.config["endpoints"]
        self.models = self.get_models()
        self.storage = Storage()
        self.cmds = CommandRegistry()

    def get_config(self):
        with open("config.json", "r") as file:
            config = json.load(file)
            file.close()
        return config

    def get_models(self):
        models = {}
        for e in self.endpoints:
            m = []
            client = OpenAI_Client(e["url"], e["key"])
            m.append(client.get_models())
            for i in m[0]:
                models[i.id] = e["url"]
        return models

    def initialize_commands(self):
        return self.cmds.load_commands()
