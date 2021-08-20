import os
import pandas as pd
from ast import literal_eval
from cdqa.utils.filters import filter_paragraphs
from cdqa.pipeline import QAPipeline
from cdqa.utils.download import download_model, download_bnpp_data
#
# download_bnpp_data(dir='./data/bnpp_newsroom_v1.1/')
# download_model(model='bert-squad_1.1', dir='./models')

df = pd.read_csv('./bnpp_newsroom-v1.1.csv', converters={'paragraphs': literal_eval})
df = filter_paragraphs(df)

cdqa_pipeline = QAPipeline(reader='data/bert_qa.joblib')
cdqa_pipeline.fit_retriever(df=df)

query = 'non-voting director'
prediction = cdqa_pipeline.predict(query)
print(prediction[0])
