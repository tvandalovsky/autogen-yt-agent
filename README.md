# AutoGen YouTube Agent

## Description
`autogen-yt-agent` is a Python package that provides an agent capable of downloading and processing YouTube videos. It includes functionalities such as extracting audio, transcribing audio with timestamps, and getting video length.

## Installation
To install the package from the GitHub repository, use the following command:

```bash
pip install autogen_ext[openai]
pip install git+https://github.com/gagb/autogen-yt-agent
```

## Usage
The following code snippet demonstrates how to use the `autogen-yt-agent` package:

```python
from autogen_yt_agent import YouTubeAgent

agent = YouTubeAgent(name='yt-agent',
                    client=)
```