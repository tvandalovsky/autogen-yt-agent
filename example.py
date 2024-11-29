import asyncio

from autogen_agentchat.task import Console, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat

# ensure autogen_ext is installed; e.g., pip install 'autogen_ext[openai]==0.4.0.dev8'
# if you want to use a different model client (e.g., anthropic), you can install
# the relevant extension instead
from autogen_ext.models import OpenAIChatCompletionClient
from autogen_yt_agent import YouTubeAgent


async def main() -> None:
    """
    Main function to run the video agent.
    """
    # Define an agent
    video_agent = YouTubeAgent(
        name="yt_agent",
        model_client=OpenAIChatCompletionClient(model="gpt-4o-2024-08-06")
        )

    # Define termination condition
    termination = TextMentionTermination("TERMINATE")

    # Define a team
    agent_team = RoundRobinGroupChat([video_agent], termination_condition=termination)

    # Run the team and stream messages to the console
    stream = agent_team.run_stream(task="Explain the keys lesson from https://www.youtube.com/watch?v=KuX_dkqr7UY")
    await Console(stream)

asyncio.run(main())
