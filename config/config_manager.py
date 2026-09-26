import json
from providers import openai_client
from config import storage_manager
from config import command_registry

class Config:

    def __init__(self):
        self.config = self.get_config()
        self.endpoints = self.config["endpoints"]
        self.models = self.get_models()
        self.storage = storage_manager.Storage()
        self.cmds = command_registry.CommandRegistry()

    def get_config(self):
        with open("config.json", "r") as file:
            config = json.load(file)
            file.close()
        return config

    def get_models(self):
        models = []
        for e in self.endpoints:
            client = openai_client.OpenAI_Client(e["url"], e["key"])
            models.append(client.get_models())
            #TODO: we should return a map of the useful model names as keys and the ctx_size as values.

    def initialize_commands(self):
        return self.cmds.load_commands()