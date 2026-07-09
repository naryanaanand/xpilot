
from openai import OpenAI

from config import Config

from logger import logger


class OpenAIClient:

    def __init__(self):

        self.client = OpenAI(
            api_key=Config.OPENAI_API_KEY
        )

    def generate(
        self,
        prompt: str,
        model: str | None = None,
    ) -> str:

        try:

            response = self.client.responses.create(

                model=model or Config.MODEL,

                input=prompt,

            )

            return response.output_text

        except Exception as e:

            logger.exception(e)

            raise
