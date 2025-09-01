from pydantic import BaseModel
from typing import List


class InsertVectorRequest(BaseModel):
    id: str
    vector: List[float]
    metadata: dict


class SearchRequest(BaseModel):
    query_vector: List[float]
    top_k: int


class SearchResultItem(BaseModel):
    id: str
    score: float
    metadata: dict


class SearchResponse(BaseModel):
    results: List[SearchResultItem]
