def solution(args):
    range_list = args
    range_list_extract = []
    for i in range(len(range_list)):
        if(i == len(range_list) - 1):
            if(range_list[i] == range_list[i-1] + 1):
                range_list_extract.append(range_list[i])
        elif(range_list[i] == range_list[i+1] - 1 or range_list[i] == range_list[i-1] + 1):
            range_list_extract.append(range_list[i])

    return range_list_extract


print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))