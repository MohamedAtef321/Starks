if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    input_list = list(arr)
    run_up_sc = sorted(list(set(input_list)))
    
    print(run_up_sc[-2])
    
