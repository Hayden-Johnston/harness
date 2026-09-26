from dotenv import load_dotenv
from config import config_manager
from agent import agent_manager
from cli import cli_manager

def main():
    load_dotenv()
    cfg = config_manager.Config()
    agent = agent_manager.Agent(cfg)
    cli = cli_manager.CLI(cfg, agent)
    print()
    cli.run()

if __name__ == "__main__":
    main()