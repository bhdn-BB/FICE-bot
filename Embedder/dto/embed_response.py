from pydantic import BaseModel


# output
class EmbedResponse(BaseModel):
    embeddings: list[list[float]]