from typing import Optional

from openai import OpenAI

from config import Config
from logger import logger


class LLM:
    """
    Wrapper around the OpenAI Responses API.

    Every agent should use this class instead of talking
    directly to OpenAI.
    """

    def __init__(self):

        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY
        )

        self.model = Config.MODEL

    def generate(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        model: Optional[str] = None,
    ) -> str:

        try:

            inputs = []

            if system_prompt:

                inputs.append(
                    {
                        "role": "system",
                        "content": [
                            {
                                "type": "input_text",
                                "text": system_prompt,
                            }
                        ],
                    }
                )

            inputs.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": prompt,
                        }
                    ],
                }
            )

            response = self.client.responses.create(
                model=model or self.model,
                input=inputs,
            )

            return response.output_text

        except Exception as e:

            logger.exception(e)

            raise
