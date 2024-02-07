
# def brute_force_n2_sub_array(arr):
#     n = len(arr)
#     for window_size in range(1, n+1):
#         left = 0
#         right = window_size
#         while(right<n+1):
#             sub_array = arr[left:right]
#             print(sub_array)
#             left+=1
#             right+=1
#
#
# brute_force_n2_sub_array([1,2,3])

def brute_force_n2_sub_array_sum(arr):
    n = len(arr)
    max_sum = -999
    for window_size in range(1, n+1):
        left = 0
        right = window_size
        while(right<n+1):
            sub_array = arr[left:right]
            max_sum = max(max_sum, (sum(sub_array)))
            left+=1
            right+=1
    return max_sum

ans = brute_force_n2_sub_array_sum([-2,-3,4,-1,-2,1,5,-3])
print(ans)
