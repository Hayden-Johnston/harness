from agent import session
from providers import openai_client

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
        self.client = openai_client.OpenAI_Client("http://172.16.1.201:8080/v1", "LLAMA_KEY", "qwen3.8-27b-fable")

    def run(self, req):
        return self.client.get_response(req)

    # TODO: implement loop logic:
    # take user input
    # integrate into LLM request
    # stream response back
    # handle tool chain
    # report tool results to LLM
    # stream response to user

    # start by writing the classic agent loop.  You can add classifiers later and DAG later.