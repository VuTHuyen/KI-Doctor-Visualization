"""
Basic audio streaming example.

This example shows how to stream the audio data from the TTS engine,
and how to get the WordBoundary events from the engine (which could
be ignored if not needed).

The example streaming_with_subtitles.py shows how to use the
WordBoundary events to create subtitles using SubMaker.
"""

import asyncio

import edge_tts

TEXT = "Hello World!"
VOICE = "en-GB-SoniaNeural"
OUTPUT_FILE = "test.mp3"


async def amain() -> None:
    """Main function"""
    communicate = edge_tts.Communicate(TEXT, VOICE)
    arr = []
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            arr.append(chunk["data"])
        elif chunk["type"] == "WordBoundary":
            print(f"WordBoundary: {chunk}")
    return arr

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()