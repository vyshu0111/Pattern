



# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def nStarDiamond(N):    # Write your code here.
    for i in range(1,N+1):
        for j in range(1,i+1):
            if((i+j)%2)!=0:
                print(0,end=" ")
            else:
                print(1,end=" ")
        print('')
            
                
            
    
n=int(input())
res=nStarDiamond(n)
print(res)
