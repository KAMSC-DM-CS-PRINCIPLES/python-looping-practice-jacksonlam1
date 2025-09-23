def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            result = i * j
            print(str(i)+"+"+str(j)+"="+str(result))
    # TODO create multiplication table function
    # HINT: Use nested for loops (for i in range(1, n + 1): for j in range(1, n + 1):)
    # HINT: Print format should be f"{i} x {j} = {result}"
    # HINT: Calculate result as i * j (not i * j + 1)
    # HINT: Use print() to display each multiplication

