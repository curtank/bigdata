from recsys import BaselineOnly
from recsys import Dataset
from recsys import evaluate
from recsys import Reader
from recsys import NormalPredictor
from recsys import KNNWithMeans
from recsys import SVD
from recsys import KNNBasic
# path to dataset file
import pickle
file_path = './3000split/train.data0'  # change this
usercluster=pickle.load(open('./cluster/0','rb'))
usercluster=dict(usercluster,**pickle.load(open('./cluster/1000','rb')))
usercluster=dict(usercluster,**pickle.load(open('./cluster/2000','rb')))
#print usercluster
# As we're loading a custom dataset, we need to define a reader. In the
# movielens-100k dataset, each line has the following format:
# 'user item rating timestamp', separated by '\t' characters.
reader = Reader(line_format='user item rating', sep=' ',rating_scale=(0, 100))

data = Dataset.load_from_file(file_path, reader=reader)

data.split(n_folds=2)
#trainset=data.build_full_trainset()
sim_options={'name':'cosine','user_based':False}
# We'll use an algorithm that predicts baseline estimates.
#algo = BaselineOnly()
#algo = NormalPredictor()
def testKNNbasic():
    for i in range(1,10):
        print 'k=',i*10
        algo=KNNBasic(k=i*10)
        #algo=SVD()
        
        evaluate(algo,data)
algo=KNNWithMeans(k=10)
#algo=SVD()

def detial(algo):
    for trainset,testset in data.folds():
        algo.train(trainset)
        predict=algo.test(testset)
        
        for s in predict:     
            if(abs(s.r0-s.est)>40):
                print s.uid,s.iid,s.r0,s.est,usercluster.get(s.uid)

from recsys import accuracy


import math
import myevaluate

for trainset,testset in data.folds():
    algo.train(trainset)
    predict=algo.test(testset)
    print accuracy.rmse(predict,verbose=True)
    print myevaluate.newdiff(predict,100)
    newgoodpred=0
    oldgoodpred=0
    import improvepredict
    newpredict,goodone,badone=improvepredict.clusterimprove(predict,usercluster)
    print goodone,badone
    print myevaluate.newdiff(newpredict,100)
    print accuracy.rmse(newpredict,verbose=True)

         
# detial(algo)
# Evaluate performances of our algorithm on the dataset.
#evaluate(algo, data)