"""There are N integers in an array A. All but one integer occur in pairs. 
The task is to find the number that occurs only once."""

def lonelyinteger(a):
    answer_list = filter(lambda x: a.count(x) == 1, a)
    answer = answer_list[0]
    return answer

if __name__ == '__main__':
    a = input()
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))
    
