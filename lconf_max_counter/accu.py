#!/usr/bin/env python3

data = open('lconf_list','r')
result = open('accu_result','w')
lconf = []
lconf.append('conf_number')
enumerator = []
i = 1
j = 0
col_num=0
for line in data :
    A = line.split()
    A[col_num]=int(A[col_num])
    if A[col_num]==lconf[-1] :
        i += 1
        continue
    else:
        lconf.append(A[col_num])
        enumerator.append(i)
        j += i
        i = 1
enumerator.append(i)
j += i
enumerator[0]='conf_repeated'
for i , conf_num in enumerate(lconf):
    if i == 0 :
        result.write(enumerator[i]),
        result.write('\t')
        result.write(conf_num),
        result.write('\n')
    else :
        result.write("    %5.4d    " % enumerator[i]),
        result.write('\t')
        result.write("   %5.5d   " % conf_num),
        result.write('\n')

print('number of total lines is :{}'.format(j-1))
data.close()
result.close()
