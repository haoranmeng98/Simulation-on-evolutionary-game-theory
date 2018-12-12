import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import random
import math
b = 2#Temptation
N = 1000#define the number of players
m = 2
G = nx.barabasi_albert_graph(N,m)
K = 0.1# Noise
MCS = 10000# Define the Monte Carlo steps
for i in range(N):
    G.nodes[i]['strategy'] = random.randint(0,1)#Initial the strategy of every player
def Cal_payoff(G,player):
    L = nx.all_neighbors(G,player)#Get all the neighbors of the choosen player
    strate = G.nodes[player]['strategy']#Get strategy of the chooosen player
    payoff  = 0#Initial the payoff
    for i in L:#Calculate the payoff
        if strate == 1:
            if G.nodes[i]['strategy'] == 1:
                payoff = payoff + 0
            else:
                payoff  = payoff + b
        else:
            if G.nodes[i]['strategy'] == 1:
                payoff = payoff + 0
            else:
                payoff  = payoff + 1
    return payoff
# Star Monte Carlo Steps
def Cal_cooperation(G):
    cooperator = 0
    for i in range(N):
        if G.nodes[i]['strategy'] == 0:
            cooperator += 1
    fraction = cooperator/N
    return fraction

for i in range(MCS):
    for i in range(N):
        player = random.randint(0,N-1)#Choose a random player 
        payoff_player = Cal_payoff(G,player)
        L = nx.all_neighbors(G,player)
        L = list(L)
        length = len(L)
        random_neighbor = L[random.randint(0,length-1)]
        payoff_neighbor = Cal_payoff(G,random_neighbor)
        if G.nodes[player]['strategy'] !=G.nodes[random_neighbor]['strategy']:
            random_num = random.random()
            try:
                Fermi_value = 1/(1+math.exp((payoff_player - payoff_neighbor)/K))
            except OverflowError:
                Fermi_value = 0
            if (random_num <= Fermi_value):
                G.nodes[player]['strategy'] = G.nodes[random_neighbor]['strategy']
    fraction = Cal_cooperation(G)
    print(fraction)








