import ffmpeg
import cv2
import whisper
import yt_dlp


def extract_audio(video_path: str, audio_output_path: str) -> str:
    """
    Extracts audio from a video file and saves it as an MP3 file.

    :param video_path: Path to the video file.
    :param audio_output_path: Path to save the extracted audio file.
    :return: Confirmation message with the path to the saved audio file.
    """
    (ffmpeg.input(video_path).output(audio_output_path, format="mp3").run(quiet=True, overwrite_output=True))
    return f"Audio extracted and saved to {audio_output_path}."


def download_youtube_video(url: str, output_path: str) -> str:
    """
    Downloads a YouTube video and saves it locally.

    :param url: URL of the YouTube video.
    :param output_path: Path to save the downloaded video.
    :return: Confirmation message with the path to the saved video file.
    """
    ydl_opts = {"outtmpl": output_path, "format": "best"}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return f"Video downloaded and saved to {output_path}"
    except Exception as e:
        return f"An error occurred: {e}"


def transcribe_audio_with_timestamps(audio_path: str) -> str:
    """
    Transcribes the audio file with timestamps using the Whisper model.

    :param audio_path: Path to the audio file.
    :return: Transcription with timestamps.
    """
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, task="transcribe", language="en", verbose=False)

    segments = result["segments"]
    transcription_with_timestamps = ""

    for segment in segments:
        start = segment["start"]
        end = segment["end"]
        text = segment["text"]
        transcription_with_timestamps += f"[{start:.2f} - {end:.2f}] {text}\n"

    return transcription_with_timestamps


def get_video_length(video_path: str) -> str:
    """
    Returns the length of the video in seconds.

    :param video_path: Path to the video file.
    :return: Duration of the video in seconds.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video file {video_path}")
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = frame_count / fps
    cap.release()

    return f"The video is {duration:.2f} seconds long."


__all__ = [
    "extract_audio",
    "download_youtube_video",
    "transcribe_audio_with_timestamps",
    "get_video_length",
]
