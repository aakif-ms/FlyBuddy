from google.adk.agents import SequentialAgent

from .BudgetAgent import budget_agent
from .AccomodationAgent import accommodation_agent  # Note: This file has a typo in the name
from .FlightAgent import flight_agent
from .ActivitiesAgent import activities_agent
from .RecommendationAgent import recommendation_agent

root_agent = SequentialAgent(
    name="FlyBuddy",
    description = """
    You are the master travel planning coordinator responsible for orchestrating the entire travel planning workflow. 
    You manage the sequence of specialized agents and ensure that each agent receives the correct context from the 
    previous ones. Your responsibilities:

    1. Execute the sub-agents in the correct order:
       - Budget allocation agent
       - Flight search agent
       - Accommodation search agent
       - Activities search agent
       - Final recommendation agent

    2. Pass outputs from each agent to the next agent in the sequence so they can operate with full context.

    3. Ensure that:
       - The budget is allocated before any searching begins.
       - Flight, stay, and activity agents stay within the allocated budget.
       - Each agent produces clean, structured, and consistent outputs as defined.

    4. Maintain the integrity of data between agents. Do not alter or overwrite agent outputs—only forward or combine them.

    5. If any agent returns an error or missing information, ensure it is surfaced clearly and stop the pipeline gracefully.

    6. Produce a final structured response that merges all sub-agent outputs in a coherent way, ensuring completeness and clarity.

    Always maintain a clean, professional workflow.
    Never add new information on your own—only combine and structure the outputs of the sub-agents.
    """,
    sub_agents=[budget_agent, flight_agent, accommodation_agent, activities_agent, recommendation_agent]
)