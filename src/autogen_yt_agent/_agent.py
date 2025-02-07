from typing import Any, Awaitable, Callable, List

from autogen_agentchat.agents import AssistantAgent
from autogen_core.components.models import ChatCompletionClient
from autogen_core.components.tools import Tool

from ._tools import (
    extract_audio,
    get_video_length,
    transcribe_audio_with_timestamps,
    download_youtube_video,
    get_video_views,
)


class YouTubeAgent(AssistantAgent):
    def __init__(
        self,
        name: str,
        model_client: ChatCompletionClient,
        *,
        tools: (List[Tool | Callable[..., Any] | Callable[..., Awaitable[Any]]] | None) = None,
        description: str = "An agent that can download and process YouTube videos.",
        system_message: (
            str | None
        ) = "You are a helpful agent that is an expert at processing YouTube videos. Reply with TERMINATE to end the conversation.",
    ):
        super().__init__(
            name=name,
            model_client=model_client,
            tools=tools
            or [
                get_video_length,
                download_youtube_video,
                extract_audio,
                transcribe_audio_with_timestamps,
                get_video_views,
            ],
            description=description,
            system_message=system_message,
        )


__all__ = ["YouTubeAgent"]
