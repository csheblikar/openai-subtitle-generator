import glob
import os
import sys
from argparse import ArgumentParser

from openai import OpenAI

client = OpenAI()


def generate_srt(input_path: str, verbose: bool = False) -> None:
    if verbose:
        print(f"[verbose] processing '{input_path}'...")

    audio_file = open(input_path, "rb")

    transcription = client.audio.transcriptions.create(
        file=audio_file, model="whisper-1", response_format="srt"
    )

    # Strip .mp3 from input_path and save as .srt
    output_path = input_path[:-4] + ".srt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(transcription)
        if verbose:
            print(f"[verbose] saved transcription to '{output_path}'")


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Generate SRT files from MP3 audio files using OpenAI's Whisper model."
    )
    parser.add_argument(
        "path",
        help="Path to the MP3 file or directory containing MP3 files.",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recursively process all MP3 files in the directory.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output.",
    )

    args = parser.parse_args()

    if os.path.exists(args.path):
        if not os.access(args.path, os.R_OK):
            print(f"error: '{args.path}' is not readable", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"error: '{args.path}' does not exist", file=sys.stderr)
        sys.exit(1)

    if args.recursive:
        if not os.path.isdir(args.path):
            print(f"error: path '{args.path}' is not a directory", file=sys.stderr)
            sys.exit(1)

        for file in glob.glob(os.path.join(args.path, "**", "*.mp3"), recursive=True):
            generate_srt(file, verbose=args.verbose)
    else:
        if not os.path.isfile(args.path):
            print(f"Path '{args.path}' is not a file", file=sys.stderr)
            sys.exit(1)

        if not args.path.lower().endswith(".mp3"):
            print("Input file must be an .mp3 file", file=sys.stderr)
            sys.exit(1)

        generate_srt(args.path, verbose=args.verbose)
