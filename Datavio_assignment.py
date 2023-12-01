def travel_circuit(gas, cost):
    n = len(gas)
    t_gas = 0
    c_gas = 0
    s_index = 0

    for i in range(n):
        t_gas += gas[i] - cost[i]
        c_gas += gas[i] - cost[i]

        if c_gas < 0:
            s_index = i + 1
            c_gas = 0

    if t_gas < 0:
        return -1
    else:
        return s_index % n


gas = [1, 2, 7, 4, 1]
cost = [3, 4, 5, 1, 2]
output = travel_circuit(gas, cost)
print("Result:", output)


