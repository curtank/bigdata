from recsys.prediction_algorithms.predictions import Prediction
def weight(a,weighta,b,weightb):
    return weighta/(weighta+weightb)*a+weightb/(weighta+weightb)*b
def clusterimprove(predict,usercluster):
    goodone=0
    badone=0
    newpredict=[]
    for s in predict:
        
        cluster=usercluster.get(s.uid)
        distarr=[abs(mean[0]-s.est) for mean in cluster[0]]
        closestmean=min(distarr)
        #print cluster
        index=distarr.index(closestmean)
        
        varience=cluster[1][index]/50
        
        #newest=1/(varience+1)*(cluster[0][index][0]+1)+varience/(1+varience)*s.est
        newest=weight(cluster[0][index][0]+1,1/(varience+0.01),s.est,1)
        if abs(newest-s.est)>10:
            
            if abs(newest-s.r0)>abs(s.r0-s.est):
                badone+=1
                #print newest,s.est,s.r0
                #print cluster  
            else:
                goodone+=1

        pred=Prediction(s.uid,s.iid,s.r0,newest,{})
        #print s
        #print pred
        
        newpredict.append(pred)
    return newpredict,goodone,badone