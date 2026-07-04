#!/usr/bin/env python3
"""
Fetch YouTube video transcripts for the experts in research/sources.md.

Run this on YOUR machine (or in Claude Code), not in a network-restricted
sandbox -- it needs live access to youtube.com.

Setup:
    pip install youtube-transcript-api yt-dlp --break-system-packages

Two collection modes are supported:
  1. FREE (default): youtube-transcript-api, no key needed, works for any
     video that has captions (auto-generated or manual).
  2. Supadata (optional): if you have a Supadata API key, set SUPADATA_API_KEY
     as an env var and pass --provider supadata. Useful when a channel has
     captions disabled and you need Whisper-based transcription instead.

Usage:
    python fetch_youtube_transcripts.py --video-id dQw4w9WgXcQ --author kevin-indig
    python fetch_youtube_transcripts.py --url "https://youtube.com/watch?v=..." --author ryan-law

Output:
    research/youtube-transcripts/<author>/<video_id>.md
    (includes title placeholder, url, fetch date, and full transcript text)
"""
import argparse
import datetime
import os
import re
import sys

OUTPUT_ROOT = os.path.join(os.path.dirname(__file__), "..", "research", "youtube-transcripts")


def extract_video_id(url_or_id: str) -> str:
    if re.fullmatch(r"[\w-]{11}", url_or_id):
        return url_or_id
    match = re.search(r"(?:v=|youtu\.be/|shorts/)([\w-]{11})", url_or_id)
    if not match:
        raise ValueError(f"Could not extract a video ID from: {url_or_id}")
    return match.group(1)


def fetch_free(video_id: str) -> str:
    from youtube_transcript_api import YouTubeTranscriptApi

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return "\n".join(f"[{seg['start']:.1f}s] {seg['text']}" for seg in transcript)


def fetch_supadata(video_id: str) -> str:
    import requests

    api_key = os.environ.get("SUPADATA_API_KEY")
    if not api_key:
        raise RuntimeError("Set SUPADATA_API_KEY env var to use the Supadata provider.")
    resp = requests.get(
        "https://api.supadata.ai/v1/youtube/transcript",
        params={"videoId": video_id},
        headers={"x-api-key": api_key},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    # Supadata returns a list of {text, offset, duration} segments under "content"
    segments = data.get("content", data)
    return "\n".join(f"[{seg.get('offset', 0)}ms] {seg.get('text', '')}" for seg in segments)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="Full YouTube URL")
    parser.add_argument("--video-id", help="Bare 11-char video ID")
    parser.add_argument("--author", required=True, help="Folder name, e.g. kevin-indig")
    parser.add_argument("--title", default="", help="Video title (optional, for the header)")
    parser.add_argument("--provider", choices=["free", "supadata"], default="free")
    args = parser.parse_args()

    source = args.url or args.video_id
    if not source:
        sys.exit("Provide --url or --video-id")

    video_id = extract_video_id(source)
    fetch_fn = fetch_free if args.provider == "free" else fetch_supadata

    try:
        transcript_text = fetch_fn(video_id)
    except Exception as exc:  # noqa: BLE001
        sys.exit(f"Failed to fetch transcript for {video_id}: {exc}")

    author_dir = os.path.join(OUTPUT_ROOT, args.author)
    os.makedirs(author_dir, exist_ok=True)
    out_path = os.path.join(author_dir, f"{video_id}.md")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# {args.title or video_id}\n\n")
        f.write(f"- Video URL: https://www.youtube.com/watch?v={video_id}\n")
        f.write(f"- Author: {args.author}\n")
        f.write(f"- Fetched: {datetime.date.today().isoformat()}\n")
        f.write(f"- Provider: {args.provider}\n\n")
        f.write("## Transcript\n\n")
        f.write(transcript_text)
        f.write("\n")

    print(f"Saved transcript -> {out_path}")


if __name__ == "__main__":
    main()
