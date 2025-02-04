def nums_sums(*args):
    negative_numbers = sum(num for num in args if num < 0)
    positive_numbers = sum(num for num in args if num > 0)
    return negative_numbers, positive_numbers

numbers = map(int, input().split())
n_sum, p_sum = nums_sums(*numbers)
print(n_sum)
print(p_sum)
if abs(n_sum) > p_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")