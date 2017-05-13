import pickle
def transitematt():
    itemAttributes=[]
    with open('./data-new/itemAttribute.txt','r') as f:
        for line in f.readlines():
            items=line.split('|')
            itemAttributes.append(items)
    print(itemAttributes[0][1])

    pickle.dump(itemAttributes,open('itemAttributes','wb'))
testdata=[]
'''
with open('./data-new/test.txt','r') as f:
    userscores={}
    for line in f.readlines():
        if '|' in line and len(userscores)>0:
            testdata.append(userscores)
            userscores={}
            items=line.split('|')
            userscores['id']=items[0]
            itemAttributes.append(items)
print(itemAttributes[0][1])
'''
def transtrain():
    with open('./data-new/train.txt','r') as f:
        userscores={}
        s=f.readlines()
        #outfile=open('train.data','w')
        userid=0
        for index in range(len(s)):
            #print(s[index])
            if userid%3000==0:
                print userid
                outfile=open('./3000split/train.data'+str(userid),'w')
                pass
            if '|' in s[index]:
                item=s[index].split('|')
                length=int(item[1])
                userid=int(item[0])
                strscores=s[index+1:index+length+1]
                #print(scores)
                scores=[]
                for strscore in strscores:
                    score=strscore.split()
                    linestr=item[0]+' '+score[0]+' '+score[1]+'\n'
                    #print(linestr)
                    outfile.write(linestr)
                #print(item[0])
        #pickle.dump(userscores,open('train.data','w'))
transtrain()
          
#print(userscores[str(0)])
#transitematt()