import os

from crewai import Crew
from agents import planner, writer, editor
from tasks import plan, edit, write

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

if __name__ == "__main__":
    crew.kickoff(inputs={"topic": "AI in healthcare"})