
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CAMINHO_ARQUIVO = "linha_monitoramento.xlsx"

@app.get("/tarefas")
def get_tarefas():
    try:
        df = pd.read_excel(CAMINHO_ARQUIVO)
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/tarefas")
def salvar_tarefas(tarefas: list[dict]):
    try:
        df = pd.DataFrame(tarefas)
        df.to_excel(CAMINHO_ARQUIVO, index=False)
        return {"ok": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
