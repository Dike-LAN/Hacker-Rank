"""Given a list of N integers, your task is to select K integers from the list such that its unfairness is minimized.
if (x1,x2,x3,…,xk) are K numbers selected from the list N, the unfairness is defined as
max(x1,x2,…,xk)−min(x1,x2,…,xk)
where max denotes the largest integer among the elements of K, and min denotes the smallest integer among the elements of K."""

n = int(input())
k = int(input())
f = n-k+1
candies = [input() for _ in range(0,n)]
candies.sort()
fairness = 10**10
for i in range(0,f):
    something = (candies[i+(k-1)]-candies[i])
    if something < fairness:
        fairness = something
   
min_diff = fairness ## Write code here to compute the answer using (n, k, candies)

print(min_diff)
