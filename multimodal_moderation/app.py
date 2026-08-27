#!/usr/bin/env python3
import os
import subprocess
import signal
import sys
import phoenix as px

from multimodal_moderation.env import PHOENIX_GRPC_PORT, PHOENIX_PORT


def _configure_console_encoding() -> None:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def main():
    _configure_console_encoding()
    os.environ.setdefault("PHOENIX_PORT", str(PHOENIX_PORT))
    os.environ.setdefault("PHOENIX_GRPC_PORT", str(PHOENIX_GRPC_PORT))
    session = px.launch_app(port=PHOENIX_PORT)

    if not session:
        raise RuntimeError("Failed to launch Phoenix session.")
    
    print(f"Phoenix UI: {session.url}")

    def signal_handler(sig, frame):
        print("\nShutting down...")
        api_process.terminate()
        chat_process.terminate()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    api_process = subprocess.Popen([sys.executable, "-m", "multimodal_moderation.fastapi_app"])
    chat_process = subprocess.Popen([sys.executable, "-m", "multimodal_moderation.gradio_app"])

    try:
        api_process.wait()
        chat_process.wait()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
