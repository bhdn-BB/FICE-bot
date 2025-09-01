from pydantic import BaseModel


# input
class EmbedRequest(BaseModel):
    query: list[str]