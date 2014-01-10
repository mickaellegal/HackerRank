# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from collections import Counter

# Reading and formating the input
input = sys.stdin.readlines()
 
data = input[1].split(' ')
data = [int(x) for x in data]

#####################
#####   MEAN    #####
#####################

def mean(data):
    return float(sum(data))/len(data)

#####################
#####  MEDIAN   #####
#####################

def median(data):
    data = sorted(data)
    if len(data) % 2 == 0:
        return float(data[len(data)/2 - 1] + data[len(data)/2])/2
    else:
        return float(data[len(data)/2])

#####################
#####   MODE    #####
#####################

def mode(data):
    #return max(set(data), key=data.count)
    # data_dic = {}
    
    # for (k,v) in Counter(data).iteritems():
    #     data_dic[k] = v
    
    # seen = set(data_dic.values())	
    
    # for k,v in data_dic.iteritems():
    #     if v == max(data_dic.values()) and v not in seen:
    #         return k
    #     else:
    #         return min(data_dic.keys())
    #         break
	
	input = Counter(data)
    common = input.most_common()
    most_common = set(x for x, count in common if count == common[0][1])
    return min(most_common)

#####################
##### VARIANCE  #####
#####################

def variance(data):
    mean = float(sum(data))/len(data)
    diff = []
    
    for i in data:
        diff.append((i-mean)**2)
    variance = (sum(diff)/len(data))**0.5 
    return round(variance,1)

#####################
##### CONFIDENCE #####
#####################

def confidence(data):
    mean = float(sum(data))/len(data)
    diff = []
    for i in data:
        diff.append((i-mean)**2)
    variance = (sum(diff)/len(data))**0.5
    
    lower = mean - 1.96 * (variance/(len(data)**0.5))
    upper = mean + 1.96 * (variance/(len(data)**0.5))
    
    lower = round(lower,1)
    upper = round(upper,1)
    return str(lower) + " " + str(upper) 

    
print mean(data)
print median(data)
print mode(data)
print variance(data)
print confidence(data)