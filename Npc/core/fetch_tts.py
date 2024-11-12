import os
import json
import edge_tts
import requests
import asyncio

# this async funtion tries to convert a text to a audio in bytes using edge_tts
async def amain(text, VOICE) -> bytes:
    communicate = edge_tts.Communicate(text, VOICE)
    audio_chunks = []
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_chunks.append(chunk["data"])
        #elif chunk["type"] == "WordBoundary":
            #print(f"WordBoundary: {chunk}")

    # Join the audio chunks into a single bytes-like object
    audio_data = b''.join(audio_chunks)
    return audio_data

def fetch_tts(text, VOICE):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(amain(text, VOICE))

if __name__ == "__main__":
    result = fetch_tts("test123")
    print(result)
