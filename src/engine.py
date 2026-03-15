import logging

class AutonomousAgent:
    """A cooperative agent capable of task decomposition."""
    def __init__(self, agent_id: str):
        self.id = agent_id
        logging.info(f"Agent {agent_id} active.")

    def collaborate(self, partner_id: str, task: str):
        return f"Agent {self.id} is working with {partner_id} on: {task}"
