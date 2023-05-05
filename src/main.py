from typing import Union
from typing import List

from fastapi import FastAPI, Header
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse

from gensim.models import KeyedVectors
from gensim.models.doc2vec import Doc2Vec
import pandas as pd

app = FastAPI()

# w2v model load
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

# 특정 기사와 비슷한 특정 기사 추천. idx 값을 기반으로 추천
@app.get("/d2v")
async def similar_word():
    model = Doc2Vec.load('model/review_d2v.model')
    # 추천 할 문서 갯수 지정
    num_recommendations = 100
    # 추천할 문서 idx 값
    consumed_doc_idx = 10
    # 선택한 문서를 기반으로 임베딩된 모델에서 추천
    similar_docs = model.dv.most_similar(consumed_doc_idx, topn=num_recommendations)
    return similar_docs

@app.get("/w2v_to_render")
async def render():
    return {"w2v_to_render": "render"}