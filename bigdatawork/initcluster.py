def getusercluster(rating):
    usercluster={}
    from sklearn.cluster import KMeans 
    for user,values in rating.iteritems():
        if int(user)%100==0:
            print user
        #print values
        feature=[[int(rat)] for item,rat in values.iteritems()]
        #print feature
        clf=KMeans(n_clusters=3)
        clf.fit(feature)
        centers=[[round(x[0],3)] for x in clf.cluster_centers_]
        #print centers
        varience=[0 for center in centers]
        for index in range(len(feature)):
            label=int(clf.labels_[index])
            dis=centers[label][0]-feature[index][0]
            #print dis
            varience[label]+=dis*dis
        from collections import Counter
        count=Counter(clf.labels_)
        for index in range(len(varience)):
            if count.get(index):
                varience[index]=(varience[index])/count.get(index)
        usercluster[user]=(centers,varience)
    return usercluster
import pickle
#print rating

    #print count
    #print varience
    #print clf.cluster_centers_
    #print clf.inertia_
    #print clf.labels_
file_path = './train.data'
for i in range(20):
    rating={}
    with open(file_path+str(i*1000),'r') as o:
        for line in o:
            word=line.split()
            if rating.get(word[0]):
                pass
            else:
                rating[word[0]]={}
            rating[word[0]][word[1]]=word[2]
    usercluster=getusercluster(rating)
    print len(usercluster)
    pickle.dump(usercluster,open('./cluster/'+str(i*1000),'wb'))
    break

