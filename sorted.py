L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(dic):
	 return dic[0]
L2 = sorted(L, key=by_name)
print L2

def by_socre(dic):
	return dic[1]
L2 = sorted(L,key=by_socre,reverse=True)
print L2



def iif(condition, true_part, false_part):  
    return true_part if condition else false_part
    #return (condition and [true_part] or [false_part])[0]  