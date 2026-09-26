import os
import openai

class OpenAI_Client:
    """
    Client to access any OpenAI compatible endpoint. Client objects are managed by Agents.
    """
    def __init__(self, url, key, model=None, ctx_size=4096):
        self.key = os.getenv(key)
        self.client = openai.OpenAI(base_url=url, api_key=self.key)
        self.model = model
        self.ctx_size = ctx_size

    def get_response(self, ctx):
        res = self.client.responses.create(
            model = self.model,
            input = ctx,
            stream = True
        )
        return res

    def get_models(self):
        return self.client.models.list()
