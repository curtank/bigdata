resu=open('userknn.txt','r')
r0=open('train.txt','r')
mat={}
from recsys.prediction_algorithms.predictions import Prediction
from recsys import accuracy
import pickle
predictions=[]
for line in r0:
    word=line.split(' ')
    mat[(word[0],word[1])]=int(word[2])
#print mat
for line in resu:
    word=line.split(',')
    #if mat.get((word[0],word[1])):
    try:
        pre=Prediction(word[0],
        word[1],
        int(mat.get((word[0],word[1]))),
        float((word[2])),
        {})
        predictions.append(pre)

    except :
        print word[0],word[1]
        #break
    #print predictions
def printout():
    for (user,item,r0,est,_) in predictions:
        print user,item,r0,est        
#printout()
usercluster=pickle.load(open('./cluster/0','rb'))
usercluster=dict(usercluster,**pickle.load(open('./cluster/1000','rb')))
usercluster=dict(usercluster,**pickle.load(open('./cluster/2000','rb')))
import improvepredict
import myevaluate

newpredictions,good,bad=improvepredict.clusterimprove(predictions,usercluster)
print 'betterchange',good
print 'worsechange',bad
print 'newprediction:'
rmse=accuracy.rmse(newpredictions,verbose=True)
print 'oldprediction:'
rmse =accuracy.rmse(predictions,verbose=True)
print myevaluate.newdiff(newpredictions,100)
print myevaluate.newdiff(predictions,100)
print usercluster.get('2')