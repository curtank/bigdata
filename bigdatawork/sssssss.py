#coding=utf-8  
from recsys import Dataset
from recsys import evaluate
from recsys import Reader
from recsys import NormalPredictor
from recsys import KNNWithMeans
from recsys import SVD
from recsys import KNNBasic

# path to dataset file
# 使用pip install recsys 可以下载相关库
# using pip install recsys will dowload all packages you needed

file_path = './train.data0'  # change this

reader = Reader(line_format='user item rating', sep=' ',rating_scale=(0, 100))

data = Dataset.load_from_file(file_path, reader=reader)

data.split(n_folds=10)
#trainset=data.build_full_trainset()
sim_options={'name':'cosine','user_based':False}
# We'll use an algorithm that predicts baseline estimates.
#algo = BaselineOnly()
#algo = NormalPredictor()

#algo=SVD()
algo=KNNBasic()

from recsys.prediction_algorithms.predictions import Prediction
from recsys import accuracy
for trainset,testset in data.folds():
    algo.train(trainset)
    predict=algo.test(testset)
    print accuracy.rmse(predict,verbose=True)      
# detial(algo)
# Evaluate performances of our algorithm on the dataset.
#evaluate(algo, data)