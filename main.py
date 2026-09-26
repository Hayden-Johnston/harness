from dotenv import load_dotenv
from config import config_manager
from agent import agent_manager
from cli import cli_manager

def main():
    print("Welcome to Hayden Agent")
    print("Setting up...")
    load_dotenv()
    cfg = config_manager.Config()
    agent = agent_manager.Agent(cfg)
    cli = cli_manager.CLI(cfg, agent)
    print("Ready to go!")
    cli.run()

if __name__ == "__main__":
    main()