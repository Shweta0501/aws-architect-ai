from openai import OpenAI

from app.config.settings import OPENAI_API_KEY
from app.models.architecture import Architecture
from app.prompts.architecture_prompt import SYSTEM_PROMPT


class AIService:

    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY is not configured."
            )

        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )

    def generate_architecture(
        self,
        requirement: str
    ) -> Architecture:

        response = self.client.responses.parse(
            model="gpt-5.6-luna",
            input=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": requirement,
                },
            ],
            text_format=Architecture,
        )

        return response.output_parsed