import multiprocessing

def find_max(nums):
    return max(nums)

if __name__ == '__main__':
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    with multiprocessing.Pool(processes=3) as pool:
        result = pool.map(find_max, nums)
    print(max(result))