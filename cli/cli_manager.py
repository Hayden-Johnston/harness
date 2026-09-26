from config import command_registry

class CLI:
    """
    Manages the CLI user interface.
    """
    def __init__(self, config=None, agent=None):
        self.cfg = config
        self.agent = agent
        self.cmds = self.cfg.cmds.cmds

    def config(self):
        pass

    def run(self):
        while(1):
            req = input()
            split_req = req.split(" ")
            head = split_req[0].strip("/")
            if split_req[0][0] == "/" and head in self.cfg.cmds.cmds:
                c = self.cfg.cmds.cmds[split_req[0].strip("/")]
                res = c.handler()
                print(res)
            else:
                try: res = self.agent.run(req)
                except: print(f"Agent call failed: Agent set to {self.agent}")
                for event in res:
                    if event.type == "response.output_text.delta":
                        print(event.delta, end="", flush=True)
                    elif event.type == "response.completed":
                        print((event.response.usage.input_tokens, event.response.usage.output_tokens))

    def cmd_handler(self, cmd: command_registry.Command):
        if cmd.name == "help":
            print(cmd.handler())
        elif cmd.name == "new":
            print(cmd.handler(self.agent))
        elif cmd.name == "compress":
            pass

    #TODO: implement slash commands (/new, /models)
    #TODO: toolchain progress
    #TODO: rich + prompt_toolkit?