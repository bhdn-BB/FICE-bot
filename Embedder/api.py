from fastapi import FastAPI
from sentence_transformers import SentenceTransformer
import uvicorn
from Embedder.config import MODEL_PATH, PORT, HOST, DEVICE
from Embedder.dto.embed_request import EmbedRequest
from Embedder.dto.embed_response import EmbedResponse

model = SentenceTransformer(MODEL_PATH, device=DEVICE)

app = FastAPI(title="Embedder Service")

@app.post("/embed", response_model=EmbedResponse)
async def embed(req: EmbedRequest):
    vectors = model.encode(req.query, normalize_embeddings=True).tolist()
    return EmbedResponse(embeddings=vectors)

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
