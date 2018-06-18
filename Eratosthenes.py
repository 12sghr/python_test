import math

def eratosthenes():
    print("数値を入力…")
    input_num = int(input())

    if input_num < 2:
        return print("素数はありません")

    prime_numbers = [2, 3, 5]
    nums = [i for i in range(2, input_num + 1) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]

    while math.sqrt(input_num) >= nums[0]:

        prime_numbers.append(nums[0])

        for i in range(nums[0], nums[-1], nums[0]):
            if i in nums:
                nums.remove(i)
                print(i)

    print(prime_numbers + nums)

eratosthenes()
