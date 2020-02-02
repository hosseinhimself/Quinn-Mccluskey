############Functions################
def ones(binary): #تابع شمارنده تعداد یک های عدد باینری
    flag=0
    for i in binary:
        if (i == '1'):
            flag=flag+1
    return flag

def combining2(elementslist): #مرحله دوم ادغام-وقتی مقدار پوشش داده نشده باقی موند
    Output = []
    combineddata1 = []
    cleandata = []
    Listcopy = list(elementslist)
    size = len(Listcopy)
    flag = [0]*size
    counter = 0
    for i in range(size):
        for j in range(i+1, size):
            c = combine( str(Listcopy[i]), str(Listcopy[j]) )
            if c != None:
                combineddata1.append(str(c))
                flag[i] = 1
                flag[j] = 1
            else:
                continue
    flag2 = [0]*len(combineddata1)
    for p in range(len(combineddata1)):
        for n in range(p+1, len(combineddata1)):
            if( p != n and flag2[n] == 0):
                if( combineddata1[p] == combineddata1[n]):
                    flag2[n] = 1
    for r in range(len(combineddata1)):
        if(flag2[r] == 0):
            cleandata.append(combineddata1[r])
    for l in range(size):
        if( flag[l] == 0 ):
            Output.append( str(Listcopy[l]) )
            counter = counter+1
    if(counter == size or size == 1):
        return Output
    else:
        return Output + combining2(cleandata)

def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
        # return string
    return str1

def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

def binary(num): #تبدیل عدد به عدد باینری
    i=bin(num)
    number=''
    length = len(i)
    for flag in range(length):
        if (flag != 0 and flag !=1):
            number += i[flag]
    while len(number)<4:
        number = '0'+ number
    return (number)

def combine(m, n): #تابع مقایسه و ترکیب
    if m != 'x' and n !='x':
        a = len(m)
        c = ''
        count = 0
        for bit in range(a):
            if(m[bit] == n[bit]):
                c += m[bit]
            elif(m[bit] != n[bit]):
                c += '-'
                count += 1
        if(count > 1):
            return None
        else:
            return c
    else:
        return None

def sort(data): #مرتب کننده لیست برای مرحله اول
    sorted = {'zero': [], 'one': [], 'two': [], 'three': [], 'four': []}
    for items in data:
        if ones(binary(items)) == 0:
            sorted['zero'].append(items)
        if ones(binary(items)) == 1:
            sorted['one'].append(items)
        if ones(binary(items)) == 2:
            sorted['two'].append(items)
        if ones(binary(items)) == 3:
            sorted['three'].append(items)
        if ones(binary(items)) == 4:
            sorted['four'].append(items)
    return sorted

def prime_imp2(List):  # چک کردن ... برای مراحل بعد از مرحله اولیه
    prime_imp = {}
    for key1, value1 in List.items():
        for key2, value2 in List.items():
            d = combine(value1, value2)
            if d != None:
                if key1 != key2:
                    if d in prime_imp.values():
                        List[key1] = 'x'
                        List[key2] = 'x'
                    else:
                        prime_imp[key1 + key2] = d
                        List[key1] = 'x'
                        List[key2] = 'x'
    return prime_imp

def Minterm(list):
    mintermslist=[]
    for item in list:
        elementmaker=[]
        if item[0]=='1':
            elementmaker.append('A')
        elif item[0]=='0':
            elementmaker.append("A'")
        if item[1]=='1':
            elementmaker.append('B')
        elif item[1]=='0':
            elementmaker.append("B'")
        if item[2]=='1':
            elementmaker.append('C')
        elif item[2]=='0':
            elementmaker.append("C'")
        if item[3]=='1':
            elementmaker.append('D')
        elif item[3]=='0':
            elementmaker.append("D'")
        mintermslist.append(listToString(elementmaker))
    mintermslist=intersperse(mintermslist,' + ')
    return listToString(mintermslist)

def Maxterm(list):
    maxtermslist=[]
    for item in list:
        elementmaker=[]
        if item[0]=='0':
            elementmaker.append('A')
        elif item[0]=='1':
            elementmaker.append("A'")
        if item[1]=='0':
            elementmaker.append('B')
        elif item[1]=='1':
            elementmaker.append("B'")
        if item[2]=='0':
            elementmaker.append('C')
        elif item[2]=='1':
            elementmaker.append("C'")
        if item[3]=='0':
            elementmaker.append('D')
        elif item[3]=='1':
            elementmaker.append("D'")
        elementmaker=intersperse(elementmaker,'+')
        maxtermslist.append(listToString(elementmaker))
    maxtermslist=intersperse(maxtermslist,' . ')
    return listToString(maxtermslist)


######################################

##################################
#Enter Minterms or Maxterms:
try:
    Data=[int(x) for x in input('Enter Elements: ').split(",")]
except:
    Data=[]
#Enter Don'tCares
try:
    dontcare=[int(x) for x in input('Enter DontCares: ').split(",")]
except:
    dontcare=[]

try:
    dataflag = str(input("1)Minterm 2)Maxterm : "))
except:
    dataflag=''

##################################

finallevel={}
level1={}
level2={}
level3={}
level4={}
prime_imp={}
Datalist=[]
danddc=Data+dontcare
for items1 in danddc:
    value=str(binary(items1))
    Datalist.append(value)
copy1=danddc.copy()
Sorted = sort(danddc)
print('Sorted Elements: ',Sorted)
for i in Sorted['zero']:
    for j in Sorted['one']:
        c=combine(binary(i),binary(j))
        if c != None:
            level1[i,j] = c
            if i in copy1:
                copy1.remove(i)
            if j in copy1:
                copy1.remove(j)

for i in Sorted['one']:
    for j in Sorted['two']:
        c=combine(binary(i),binary(j))
        if c != None:
            level1[i,j] = c
            if i in copy1:
                copy1.remove(i)
            if j in copy1:
                copy1.remove(j)

for i in Sorted['two']:
    for j in Sorted['three']:
        c=combine(binary(i),binary(j))
        if c != None:
            level1[i,j] = c
            if i in copy1:
                copy1.remove(i)
            if j in copy1:
                copy1.remove(j)


for i in Sorted['three']:
    for j in Sorted['four']:
        c=combine(binary(i),binary(j))
        if c != None:
            level1[i,j] = c
            if i in copy1:
                copy1.remove(i)
            if j in copy1:
                copy1.remove(j)

print('1st Combine: ',level1)
level2=prime_imp2(level1)
if len(level2.values())>0:
    print('2nd Combine: ',level2)

for i in level1.items():
    if i[1] != 'x':
        finallevel[i[0]]=i[1]

for i in level2.items():
    if i[1] != 'x':
        finallevel[i[0]]=i[1]

for i in level3.items():
    if i[1] != 'x':
        finallevel[i[0]]=i[1]

for i in level4.items():
    if i[1] != 'x':
        finallevel[i[0]]=i[1]

PIs= finallevel.copy()
for item in copy1:
    PIs[item]=binary(item)
print("PIs: ", PIs)
cleardata=[]
MergedTuple=()
combin=combining2(Datalist)
for tuples in finallevel.keys():
    MergedTuple=tuples + MergedTuple
for number in MergedTuple :
    if MergedTuple.count(number)==1:
        if number in Data:
            cleardata.append(number)

FINAL=[]
for clearnumber in cleardata:
    for keys in finallevel.keys():
        if clearnumber in keys:
            FINAL.append(finallevel[keys])
for item in copy1:
    if item in Data:
        FINAL.append(binary(item))
FINAL=list(dict.fromkeys(FINAL))
print('EPIs: ',FINAL)
for o in combin:
    if o not in FINAL:
        FINAL.append(o)
if FINAL[0]=='----':
    if Data==[]:
        FINAL[0]='0'
    else:
        FINAL[0] = '1'

print('Answer: ',FINAL)

##########################################

if dataflag == '1' and FINAL[0] != '1' and FINAL[0]!='0':
    print('The Answer is: ',Minterm(FINAL))
elif dataflag== '2' and FINAL[0] != '1' and FINAL[0]!='0':
    print('The Answer is: ',Maxterm(FINAL))
elif  FINAL[0] == '1':
    print('The Answer is: 1')
elif FINAL[0]=='0':
    print('The Answer is: 0')

input('Press Enter To Continue...')