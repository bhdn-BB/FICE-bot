from pydantic import BaseModel


# input
class EmbedRequest(BaseModel):
    texts: list[str]