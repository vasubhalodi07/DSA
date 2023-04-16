def jobscheduling(jobs,t,n):
    job=['']*t
    result=[False]*t  #track of whether the job is done or not for a particular timeframe
    indices=list(range(n))
    indices.sort(key=lambda i:jobs[i][2],reverse=True)# sort indices based on profit
    #to check deadline and assign job in empty timeframe
    for i in indices:
        for j in range(jobs[i][1]-1,-1,-1):
            if(result[j] is False):
                job[j]=jobs[i][0]
                result[j]=True
                break
    return job

jobs = [['a',2,100],['b',1,19],['c',2,27],['d',1,35],['e',3,72],['f',2,50]]

n = len(jobs)
t = -1
for i in range(n):  #To find the maximum deadline
    t = max(t,jobs[i][1])

job = jobscheduling(jobs,t,n)
print("The job list sequence: ",job)
