import sys
from agent import agent_manager
from agent import session

def exit():
    print("Shutting down...")
    sys.exit(0)

def help(command=None):
    return "helping"

def new(agent: agent_manager.Agent):
    agent.session = session.Session()

def compress(agent: agent_manager.Agent):
    pass
