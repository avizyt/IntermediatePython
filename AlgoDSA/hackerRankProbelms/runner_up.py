'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.
'''

def runner_up(arr):
    highest = 0
    second = 0
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        if sorted_arr[i] > highest and sorted_arr[i] != highest:
            highest = sorted_arr[i]
            second = highest
    return f'Highest={highest} and Second={second}'










if __name__ == "__main__":
    arr = [2,3,6,6,5]
    print(runner_up(arr))