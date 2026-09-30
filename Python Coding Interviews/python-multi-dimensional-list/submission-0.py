from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    answer_list = []
    for i in range(len(nested_arr)):
        max_of_sublist = nested_arr[i][0]
        for j in range(len(nested_arr[i])):
            max_of_sublist = max(max_of_sublist, nested_arr[i][j])
        answer_list.append(max_of_sublist)
    return answer_list

# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
