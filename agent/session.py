class Session:
    """
    Session handler that is passed to agents.  Manages context window through compression and summarization.
    Parameters:
    ctx: existing context to start a session.
    """
    def __init__(self):
        self.ctx = []

    def append_ctx(self, new):
        self.ctx.append(new)

    def set_ctx(self, new):
        self.ctx = new

    #TODO: consider context structure when appending new messages.