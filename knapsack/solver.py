#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)
    # print("Capacity: " , capacity)
    # for i in range(len(items)):
    #     print(items[i],items[i].weight)
    for item in items:
        print(item)
    taken=dynamic_tabular(capacity,items)
    for i in range(len(taken)):
        value+=taken[i]*items[i].value
    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

def dynamic_tabular(k,items):
    resoult=[0]*len(items)
    table=np.zeros([k+1,len(items)+1])
    for i in range(len(items)):

        for j in range(k+1):
            if(j>=items[i].weight):
                table[j][i+1]=max(table[j][i],items[i].value+table[j-items[i].weight][i])
            else:
                table[j][i+1]=table[j][i]
    j=k
    for i in reversed(range(1,len(items)+1)):
        if(table[j][i]!=table[j][i-1]):
            resoult[i-1]=1
            j-=items[i-1].weight
        
    return resoult


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

