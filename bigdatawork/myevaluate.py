import math
def goodones(prediction,goodrange):
    goodcount=0
    for _,_,r0,est,_ in prediction:
        if abs(r0-est)<goodrange:
            goodcount+=1
    return goodcount/len(prediction)

def sigmoid(s):
    return (1/(1+math.e**(-s))-0.5)*2
def log1to11(s):
    return math.log(s+1)/math.log(11)
def newdiff(prediction,ratingrange):
    re=0
    for _,_,r0,est,_ in prediction:
        re+=log1to11(abs(r0-est)/ratingrange*30)
    print len(prediction)
    return re/len(prediction)
def transsigmoid(q):
    return -math.log(1/(q/2+0.5)-1)/math.log(math.e)
def main():
    
    for i in range(10):
        print sigmoid(i*0.5)

if __name__ == '__main__':
    main()
