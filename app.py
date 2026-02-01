from fastapi import FastAPI, Query
from pydantic import BaseModel
import re

app = FastAPI(title="Symbol Counter", version="v1")

class Health(BaseModel):
    ok: bool

class SymbolCountResponse(BaseModel):
    input: str
    symbol_count: int

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/symbol-count", response_model=SymbolCountResponse)
def symbol_count(text: str = Query(..., description="Text to count symbols for")):
    # Count printable characters that are not letters, digits, or whitespace
    symbols = re.findall(r"[^\w\s]", text)
    return {"input": text, "symbol_count": len(symbols)}
