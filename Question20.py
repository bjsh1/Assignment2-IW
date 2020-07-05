#20. Write a Python class to find the three elements that sum to zero 
# from a list of n real numbers. 
# Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
# Output : [[-10, 2, 8], [-7, -3, 10]]

if __name__ == '__main__':
    input_list = [-25, -10, -7, -3, 2, 4, 8, 10]
    expected_ans = 0
    input_list.sort()
    expected_ans_num_list = []
    for i in range(len(input_list)):
        if input_list[i] >= expected_ans:
            break
        for j in range(i + 1, len(input_list)):
            if input_list[i]+input_list[j] >= expected_ans:
                break
            for k in range(j + 1, len(input_list)):
                c_sum = input_list[i] + input_list[j] + input_list[k]
                if c_sum > expected_ans:
                    break
                elif c_sum == expected_ans:
                    expected_ans_num_list.append([input_list[i], input_list[j], input_list[k]])
                    break

    print(expected_ans_num_list)