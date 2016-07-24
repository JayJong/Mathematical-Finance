from __future__ import division
import numpy as np
import math
import time

#to calculate time
##start = time.time()
##code...
##end = time.time()
##print(end - start)



################################################################## Qn 1 ######################################################################

def binomialtree(option, K, T, S, sigma, r, q, n, Exercise):
    delta = T / n 
    u = math.exp(sigma * math.sqrt(delta))
    d = 1 / u
    p0 = (math.exp((r - q) * delta) - d) / (u - d)
    p1 = 1 - p0

#creating the tree   
    tree = {}
    for i in range(n + 1):
        listofprice = []
        for j in range(n + 1):
            if i >= j:
                listofprice.append(S * u ** (i-j) * d ** j)
        tree[i] = listofprice

#find the option value at final node depending on call or put
    backtree = {}
    if option == 'call':
        finalnodes = []
        for i in tree[n]:
            finalnodes.append(max(i - K, 0))
        backtree[n] = finalnodes
    else:
        finalnodes = []
        for j in tree[n]:
            finalnodes.append(max(K - j, 0))
        backtree[n] = finalnodes

#option price at first node depending on American or European
    while n != 0:
        optlist = []
        for i in range(len(tree[n - 1])):
            if Exercise == 'A':
                if option == 'call':
                    optlist.append(max(tree[n - 1][i] - K, math.exp(-r * delta) * (p0 * backtree[n][i] + p1 * backtree[n][i + 1])))
                else:
                    optlist.append(max(K - tree[n - 1][i], math.exp(-r * delta) * (p0 * backtree[n][i] + p1 * backtree[n][i + 1])))
            else:
                optlist.append(math.exp(-r * delta) * (p0 * backtree[n][i] + p1 * backtree[n][i + 1]))
        backtree[n - 1] = optlist
        n = n - 1
        

##    print tree
##    print finalnodes
##    print backtree[0][0]
    return backtree[0][0]






################################################################## Qn 2 ######################################################################

##start = time.time()
##
for i in range(1,18201,1001):
    print i, binomialtree('call', 100, 1, 100, 0.2, 0.05, 0.04, i, 'E')
##end = time.time()
##print "Time Taken:", (end - start)


################################################################## Qn 3 ######################################################################

start = time.time()



# Put value as a function of initial stock price
##
for i in range(0,210, 10):
    print i, binomialtree('put', 100, 1, i, 0.2, 0.05, 0, 2050, 'A')


# To find S*

##i = 100
##while abs(100 - i - binomialtree('put', 100, 1, i, 0.2, 0.05, 0, 2050, 'A')) >= 0.005:
##    i -= 10
##
##
##i = i + 10
##while abs(100 - i - binomialtree('put', 100, 1, i, 0.2, 0.05, 0, 2050, 'A')) >= 0.005:
##    i -= 1
##
##
##i = i + 1
##while abs(100 - i - binomialtree('put', 100, 1, i, 0.2, 0.05, 0, 2050, 'A')) >= 0.005:
##    i -= 0.1
##
##i = i + 0.1
##while abs(100 - i - binomialtree('put', 100, 1, i, 0.2, 0.05, 0, 2050, 'A')) >= 0.005:
##    i -= 0.01
##
##i = i + 0.01
##while abs(100 - i - binomialtree('put', 100, 1, i, 0.2, 0.05, 0, 2050, 'A')) >= 0.005:
##    i -= 0.001
##print i



def optimalput(T, q):
    i = 100
    for m in [10, 1, 0.1, 0.01, 0.001]:
        while abs(100 - i - binomialtree('put', 100, T, i, 0.2, 0.05, q, 2050, 'A')) >= 0.005:
            i -= m
        if m != 0.001:
            i = i + m
        else:
            print "S_0:", i, "put price:", binomialtree('put', 100, T, i, 0.2, 0.05, q, 2050, 'A')



print "q = 0"
for j in range(1, 13):
    optimalput(j / 12, 0)

print "q = 0.04"
for j in range(1, 13):
    optimalput(j / 12, 0.04)


 
end = time.time()
print "Time Taken:", (end - start)

################################################################## Qn 4 ######################################################################

##Call value as a function of initial stock price

for i in range(0,220, 10):
    print i, binomialtree('call', 100, 1, i, 0.2, 0.05, 0.04, 2050, 'A')


def optimalcall(T, q):
    i = 100
    for m in [10, 1, 0.1, 0.01, 0.001]:
        while abs(i - 100 - binomialtree('call', 100, T, i, 0.2, 0.05, q, 2050, 'A')) >= 0.005:
            i += m
        if m != 0.001:
            i = i - m
        else:
            print "S_0:", i, "call price:", binomialtree('call', 100, T, i, 0.2, 0.05, q, 2050, 'A')

print "q = 0.04"
for j in range(1, 13):
    optimalcall(j / 12, 0.04)

print "q = 0.08"
for j in range(1, 13):
    optimalcall(j / 12, 0.08)





##########################################################################################################################################


