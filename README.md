# Philosophy
A minimal harness to serve as a foundation for further AI improvement.
Most harnesses are not built around the limitations of local models, the user drops in their provider credentials and the agentic loop performs an LLM request between every set of tool calls before providing the final response.
Jev is trending this week as a general classification model with extremely low latency and cost.  Such a classification model can be used in between tool calls to make decisions on the next actions the agent should take.
This way we can specify tool chains with branching based on a classification model output.  The initial LLM response may build the tool chain where tool outputs are used to make a decision or to craft a response.  Where classification is used, the tool outputs fed to it must be contextualized by the LLM when the tool chain is initially generated.
Building tool chains to define the thought process in advance eliminates reasoning time from intermediate LLM calls which is offloaded to low latency classification models.

# Toolchain Schema
Toolchains can be defined as graphs.  A set of tools can be ran in parallel before a classification step.  The classification determines if another tool set runs, the decision is escalated, or the final output is generated.