sum = 0
def add_num(a,n):
    s = set() 
      
    for i in range(0, len(a)): 
        if sum-a[i]  in s: 
            print ("Pair with given sum "+ str(sum) + " is (" + str(a[i]) + ", " + str(sum-a[i]) + ")")
        s.add(a[i]) 

a = list(map(int, input().split()))
n = int(input())
add_num(a,n)
