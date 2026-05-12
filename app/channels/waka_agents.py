from app.integrations.foundry_agents import FoundryAgentsClient
async def run_agent(settings, token, agent_id, payload):
    return await FoundryAgentsClient(settings, token).run(agent_id, payload)
