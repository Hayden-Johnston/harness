import sys
from agent.agent_manager import Agent
from agent.session import Session

def exit():
    print("Shutting down...")
    sys.exit(0)

def help(command=None):
    if command == None:
        return "syntax /help [command]: No valid command detected."
    return "helping"

def new(agent: Agent):
    agent.session = Session()
    return "New session initialized"

def compress(agent: Agent):
    pass
