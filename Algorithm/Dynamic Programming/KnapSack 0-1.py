def KnapSack01(profit,weight,capacity):
    index = list(range(len(profit)))
    ratio = [p/w for p,w in zip(profit,weight)]
    index.sort(key=lambda i:ratio[i],reverse=True)
    fraction=[0]*len(profit)
    total_profit = 0

    for i in index:
        if weight[i]<=capacity:
            fraction[i] = 1
            capacity = capacity-weight[i]
            total_profit = total_profit+profit[i]
    return total_profit,fraction

profit = [100,60,120]
weight = [20,10,30]
capacity = 50
profit, fraction = KnapSack01(profit, weight, capacity)
print(profit, fraction)
