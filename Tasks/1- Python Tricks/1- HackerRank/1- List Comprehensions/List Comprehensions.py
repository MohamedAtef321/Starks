if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    vec_list = []
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                #if (i+j+k!=n): vec_list.append([i,j,k])
                vec_list.append([i,j,k])
    
    out_vecs = [vec for vec in vec_list if sum(vec)!=n]
                
    print(out_vecs)
