import os

from fastapi import FastAPI, Header
from fastapi.middleware.cors import CORSMiddleware

from gensim.models import KeyedVectors
from gensim.models.doc2vec import Doc2Vec
import pandas as pd
import json
from dotenv import load_dotenv

import boto3
import pickle

from utils import log

app = FastAPI()

# env 파일 업로드
load_dotenv()

access_key = os.getenv("AWS_KEY")
secret_key = os.getenv("AWS_SECRET_KEY")

s3 = boto3.resource('s3',
                  aws_access_key_id=access_key,
                  aws_secret_access_key=secret_key)

bucket = s3.Bucket('hangle-square')
model_file = 'recsys_model/review_w2v'
local_model_path = 'model/review_w2v_test'

bucket.download_file(model_file, local_model_path)

# 로그찍는법 : logger.info("로그 표시할 내용")
logger = log()

# 모델 로드
try:
    loaded_model = KeyedVectors.load_word2vec_format(local_model_path)
except KeyError:
    print("입력된 단어에 대한 유사 단어를 찾을 수 없습니다.")

# cors에러 방지
origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#test
# bucket = 'hangle-square'
# s3_dir = 'recsys_model/review_w2v'


# w2v model load
@app.get("/")
async def read_root():
    model_result = loaded_model.most_similar("항공사")

    # 추천 리스트
    recList = []
    for res in model_result:
        word, score = res
        recList.append({'word': word, 'score': score})
    return recList
    # # 모델 로드
    # loaded_model = KeyedVectors.load_word2vec_format("model/review_w2v")
    # # 키워드 기반 추천
    # model_result = loaded_model.most_similar("미국")
    # # 추천 리스트
    # recList = []
    # for res in model_result:
    #     word, score = res
    #     recList.append({'word': word, 'score': score})
    # return recList

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