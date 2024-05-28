from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from crewai_tools import YoutubeChannelSearchTool
import os
os.environ["OPENAI_API_KEY"] = "NA"
llm = ChatOpenAI(
    model="crewai-llama3",
    base_url="http://localhost:11434/v1"
)

tool = YoutubeChannelSearchTool(
    config=dict(
        llm=dict(
            provider="ollama",
            config=dict(
                model="llama3",
            ),
        ),
        embedder=dict(
            provider="huggingface",
            config=dict(
                model="sentence-transformers/msmarco-distilbert-base-v4",
                
            ),
        ),
    ),
    youtube_channel_handle='@quick_lab'
)

youtub_guy = Agent(
    role='Youtube Video Link Generator',
    goal='Extract links to the videos that solves the problem of user',
    backstory="""You are a YouTube channel specialist and content recommender.
    You are responsible for fetching links of the best videos that will satisfy the needs of the user.
    You are currently working on the channel which deals with videos that help users to solve labs on Google Cloud Quicklabs.
    """,
    tools=[tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

search_task = Task(
    description='Find me a video that will help me solve the Arcade Hero: Enter the Artifact Registry Container',
    expected_output='Link to the video',
    agent=youtub_guy
)

my_crew = Crew(
    agents=[youtub_guy],
    tasks=[search_task],
    verbose=True
)

result = my_crew.kickoff()

print(result)
