salarys = [200, 250, 320, 413, 516, 680, 791, 877, 999, 1000, 2000, 3000]
salary_count = [0] * 9
for salary in salarys:
    index = salary // 100 -2
    max_index = len(salary_count) -1
    index = min(index, max_index)
    salary_count[index] += 1

print(salary_count)
