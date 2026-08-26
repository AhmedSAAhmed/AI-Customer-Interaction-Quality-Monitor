# AI Customer Interaction Quality Monitor

This project is a training tool for customer support teams.

It helps a business check if messages, images, videos, and audio are safe and professional before they are sent to a customer.

## What It Does

- A support agent can chat with a pretend ACME customer.
- The app checks the agent's text before the customer sees it.
- The app can also check uploaded images, videos, and audio.
- If something looks unsafe, rude, unprofessional, or has private information, the app blocks it.
- The app shows feedback so the support agent can learn what to fix.
- Phoenix tracing records what happened, so a team can review the quality of the interaction.

## Why This Helps A Real Business

Customer support teams talk to many people every day. Mistakes can hurt customers and the company.

This project can help a business:

- Keep customer replies friendly and professional.
- Stop private information from being shared by mistake.
- Train new support agents in a safe practice chat.
- Review bad conversations and learn from them.
- Check images, videos, and audio, not only text.
- Improve customer trust by catching problems early.

## Example

A support agent writes:

> Here is the customer's phone number.

The moderation system can flag this because phone numbers are private information.

The agent then gets feedback and can rewrite the message before sending it.

## Main Parts

- `multimodal_moderation/gradio_app.py` runs the chat interface.
- `multimodal_moderation/fastapi_app.py` runs the moderation API.
- `multimodal_moderation/agents/` contains the AI agents for text, image, video, audio, and customer chat.
- `evals/` contains tests that check if the moderation agents are making good choices.
- Phoenix shows traces so you can see what the app did step by step.

## Setup

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=your-gemini-api-key
USER_API_KEY=choose-a-local-api-key
DEFAULT_GOOGLE_MODEL=gemini-2.5-flash
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the full app:

```bash
multimodal-moderation
```

Open:

- Chat UI: `http://localhost:7860`
- Phoenix UI: `http://localhost:6006`
- API: `http://localhost:8000`

## Local Mock Mode

For quick testing without real Gemini calls, set:

```env
MOCK_AI=true
```

Mock mode is only for checking the app flow. Real business testing should use a valid Gemini API key.

## Tests

Run tests with:

```bash
pytest
```

Run evals with:

```bash
python evals/text/test_cases.py
python evals/image/test_cases.py
```
