# -*- coding: utf-8 -*-
"""A simple example for conversation between user and assistant agent."""
import agentscope
from agentscope.agents import DialogAgent
from agentscope.agents.user_agent import UserAgent
from agentscope.pipelines.functional import sequentialpipeline

agentscope.init(
    model_configs=[
        {
            "type": "openai",
            "name": "gpt-3.5-turbo",
            "api_key": "xxx",  # Load from env if not provided
            "organization": "xxx",  # Load from env if not provided
            "generate_args": {
                "temperature": 0.5,
            },
        },
        {
            "type": "post_api",
            "name": "my_post_api",
            "api_url": "https://xxx",
            "headers": {},
        },
    ],
)

# Init two agents
dialog_agent = DialogAgent(
    name="Assistant",
    sys_prompt="You're a helpful assistant.",
    model="gpt-3.5-turbo",  # replace by your model config name
)
user_agent = UserAgent()

# start the conversation between user and assistant
x = None
while x is None or x.content != "exit":
    x = sequentialpipeline([dialog_agent, user_agent], x)