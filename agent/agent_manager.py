from agent import session
from providers.openai_client import OpenAI_Client
class Agent:
    """
    Agent identity handler for main and subagents. Agents manage their own sessions.
    Parameters:
    system = system prompt that defines an overarching system goal.
    identity = agent identity prompt to direct its behavior modes.
    """
    def __init__(self, system=None, identity=None):
        self.system = system
        self.system = identity
        self.session = session.Session()
        self.model = "qwen3.8-27b-fable"
        self.endpoint = "http://172.16.1.201:8080/v1"
        self.api_key = "LLAMA_KEY"
        self.client = OpenAI_Client(self.endpoint, self.api_key, self.model)

    def run(self, req):
        return self.client.get_response(req)

    # TODO: implement loop logic:
    # take user input
    # integrate into LLM request
    # stream response back
    # handle tool chain
    # report tool results to LLM
    # stream response to user

    # start by writing the classic agent loop.  You can add classifiers and DAG later.