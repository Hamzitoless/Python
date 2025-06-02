count=0

for i in range(1, 10):
    if i % 2 == 0:
        count += 1
        print(f"{i} is even")

print(f"Total even numbers: {count}")
