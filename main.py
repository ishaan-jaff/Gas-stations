"""
There are n
n
 gas stations along a circular route, where the amount of gas at the i^{th}
i 
th
 
 station is gas[i].

We have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the i^{th}
i 
th
 
 station to its next (i+1)^{th}
(i+1) 
th
 
 station. We begin the journey with an empty tank at one of the gas stations.

Given two integer arrays, gas and cost, return the starting gas station’s index if we can travel around the circuit once in the clockwise direction. Otherwise, return −1
−1
.

If there exists a solution, it is guaranteed to be unique.
[1,2,3,4,5] , [3,4,5,1,2])
[-2, -2, -2, 3, 3]: possible if sum(net) == 0


[5,0,2,4,5] , [1,20,1,1,2])

[4, -20, 1, 10, 5]=> left: -16, right: 16
[]
[]
[]


[-2, -2, -2, 3, 3]
[-2, -4, -6, -3, 0]
[4,2,0,3,6] when starting from 

3, 6, 4, 2, 0, 

3, 1, 




only can start from points with +ve
"""

def is_possible(i, net_balance):
  running_sum = net_balance[i]
  for idx in range(i+1, len(net_balance)):
    running_sum += net_balance[idx]
    if running_sum < 0:
      return False
  for idx in range(0, i):
    running_sum += net_balance[idx]
    if running_sum < 0:
      return False
  return True
    

def gas_station_journey(gas, cost):
  print(gas, cost)
  # brute force, go though each starting point and check if you can complete a round trip 

  net_balance = []
  for i, elem in enumerate(gas):
    net_balance.append(elem - cost[i])
  print(net_balance)
  

  for i, elem in enumerate(net_balance):
    if elem >=0 and is_possible(i, net_balance):
      return i
  
  return -1


print(gas_station_journey([1,2,3,4,5] , [3,4,5,1,2]))