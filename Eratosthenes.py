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

    print(prime_numbers + nums)

eratosthenes()

def prime(n):
    seq = list(range(2, n))
    while len(seq) > 0:#リストのlen
        prime = seq.pop(0)
        yield prime
        # 素数で割り切れない数字のリストを作成
        seq = [i for i in seq if not i % prime == 0]
print(list(prime(20)))
