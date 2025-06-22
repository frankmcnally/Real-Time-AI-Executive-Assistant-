import time
from .audio.capture import record_audio
from .transcribe.whisper_wrapper import transcribe_audio
from .utils.context_buffer import update_context
from .llm.gpt_engine import generate_insight
from .tts.elevenlabs_tts import speak


context = []

print("[AI Assistant] Listening to Zoom...")

try:
    while True:
        # 1. Record audio chunk
        audio = record_audio(duration=5)

        # 2. Transcribe
        text = transcribe_audio(audio)
        if text.strip():
            print("[Transcript]", text)
            context = update_context(text)

            # 3. Occasionally generate insight (e.g. every N turns or by keyword)
            if len(context) % 4 == 0:  # Every 4 utterances
                insight = generate_insight(context)
                print("[AI Insight]", insight)

                # 4. Speak it aloud
                speak(insight)

        time.sleep(1)  # Optional delay for control

except KeyboardInterrupt:
    print("\n[AI Assistant] Stopped.")