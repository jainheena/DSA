#User function Template for python3

def getMinMax( a, n):
    mine = 1000000000000
    maxe = 0
    for i in range(n):
        if a[i]>=maxe:
            maxe = a[i]
    
    for i in range(n):
        if a[i]<mine:
            mine=a[i]
    ans = [mine,maxe]
    return ans
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends