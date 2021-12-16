def bfs(src, target):
    arr = [src]
    c = 0
    while arr:
        c += 1                                           
        print(arr[0])
        if arr[0] == target:                     
            return 'Found with {} iterations'.format(c)
        arr += possible_moves(arr[0])                  
        arr.pop(0)                                    
    return 'Not Found'                                  
def possible_moves(state):            
    b = state.index(-1)                             
    d=[]                                            
    pos_moves=[]                                 
    if b<=5:                                       
        d.append('d')
    if b>=3 :                                        
        d.append('u')
    if b%3 > 0:                                     
        d.append('l')
    if b%3 < 2:                                     
        d.append('r')
    for i in d:                                      
        temp = gen(state, i, b)                      
        pos_moves.append(temp)                       
    return pos_moves                                 
def gen(state, m, b):                               
    temp=state.copy()                               
    if m == 'l':                                    
        temp[b], temp[b-1] = temp[b-1], temp[b]      
    if m == 'r':                                    
        temp[b], temp[b+1] = temp[b+1], temp[b]
    if m == 'u':                                    
        temp[b], temp[b-3] = temp[b-3], temp[b]
    if m =='d':                                     
        temp[b], temp[b+3] = temp[b+3], temp[b]
    return temp
src=[1,2,3,-1,4,5,6,7,8]
target=[1,2,3,6,4,5,-1,7,8]
print(bfs(src, target))
