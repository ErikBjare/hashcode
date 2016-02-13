__author__ = 'jra'

stat = list(map(int, input().split()))
prodn = int(input())
prodw= list(map(int, input().split()))
waren = int(input())

whs = []
for i in range(waren):
    whs.append([])
    whs[i].append(list(map(int, input().split())))
    whs[i].append(list(map(int, input().split())))

ordern = int(input())
orders = []

for i in range(ordern):
    orders.append([])
    orders[i].append(list(map(int, input().split())))
    orders[i].append(int(input()))
    orders[i].append(list(map(int, input().split())))

def simdrone(commands):
    
