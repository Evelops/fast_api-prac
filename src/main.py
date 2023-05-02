from typing import Union
from typing import List

from fastapi import FastAPI, Header
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from gensim.models import KeyedVectors

app = FastAPI()

@app.get("/")
async def read_root():
    # 모델 로드
    loaded_model = KeyedVectors.load_word2vec_format("model/news_w2v_2")
    # 키워드 기반 추천
    model_result = loaded_model.most_similar("한국")
    # 추천 리스트
    recList = []
    for res in model_result:
        word, score = res
        recList.append({'word': word, 'score': score})
    return recList
