import json

class Storage:

    def __init__(self):
        self.file = "metrics.json"

    def update_tokens(self, count, model=None):
        metrics = self.load_metrics()
        usage = metrics["usage"]
        usage["total_tok_in"] += count[0]
        usage["total_tok_out"] += count[1]
        if model != None and model in usage["models"]:
            usage["models"][model]["tok_in"] += count[0]
            usage["models"][model]["tok_out"] += count[1]
        elif model != None and model not in usage["models"]:
            usage["models"][model] = {"tok_in": count[0], "tok_out": count[1]}

        with open(self.file, "w") as file:
            json.dump(metrics, file, indent=4)

    def load_metrics(self):
        with open(self.file, "r") as file:
            return json.load(file)
