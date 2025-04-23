name: str = "John Doe"
age: int = 20
aggregate: float = 77.9
is_raining: bool = False

x: tuple = (1, 2, 3,)
list_names: list = ["John", "Mary"]
nums: list = [1, 2, 3, 4, 5]

data: dict = {'name': 'Bob', 'age': 25}
print(data)
print(nums)


def get_largest(numbers, n):
    numbers.sort()
    return numbers[-n]

sorted_list = get_largest(nums, 3)
#print(sorted_list)
#list comprehension


