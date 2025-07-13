# openai-subtitle-generator

**openai-subtitle-generator** is a command-line utility for generating `.srt` subtitle files from `.mp3` and `.mp4` files using OpenAI’s Whisper speech-to-text model. It is designed to be simple, efficient, and easily integrable into audio processing workflows.

## Overview

openai-subtitle-generator reads `.mp3` and `.mp4` files and transcribes them into `.srt` (SubRip Subtitle) format using OpenAI’s `whisper-1` model. It supports both single-file and batch processing modes, with optional verbosity for detailed logging.

## Features

- Converts `.mp3` and `.mp4` files into `.srt` subtitle format
- Supports batch processing via recursive folder traversal
- Verbose mode for detailed logging
- Minimal dependencies and easy setup
- Cross-platform support via Python

## Prerequisites

- Python 3.7 or higher
- OpenAI API Key

Install the required Python package:

```bash
pip install openai
```

## Usage

### Transcribe a single audio file:

```bash
python generate_srt.py path/to/audio.mp3
```

### Transcribe all .mp3 files in a folder recursively:

```bash
python generate_srt.py path/to/folder -r
```

### Enable verbose mode:

```bash
python generate_srt.py path/to/audio.mp3 -v
```

Output .srt files will be saved in the same directory as the input files, using the same base filename.
