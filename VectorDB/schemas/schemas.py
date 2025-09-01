from pydantic import BaseModel
from typing import List, Dict


class InsertVectorRequest(BaseModel):
    id: str
    vector: List[float]
    metadata: Dict


class SearchRequest(BaseModel):
    query_vector: List[float]
    top_k: int


class SearchResultItem(BaseModel):
    id: str
    score: float
    metadata: Dict


class SearchResponse(BaseModel):
    results: List[SearchResultItem]
