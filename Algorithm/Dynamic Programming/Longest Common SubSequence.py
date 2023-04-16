def lcs(X,Y):
    m = len(X)
    n = len(Y)
    L = [[0 for i in range(n+1)] for j in range (m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if(X[i-1] == Y[j-1]):
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]
            
X="sdhswawd"
Y="dfwehfuhewufc"
print("The length of longest common subsequence between X and Y is: ",lcs(X,Y))
