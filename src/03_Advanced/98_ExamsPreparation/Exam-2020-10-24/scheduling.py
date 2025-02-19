jobs = [int(n) for n in input().split(", ")]
index = int(input())

target_job = jobs[index]
sorted_jobs = sorted((val, i) for i, val in enumerate(jobs))

clock_cycles = 0
for value, i in sorted_jobs:
    clock_cycles += value
    if i == index and value == target_job:
        break

print(clock_cycles)

