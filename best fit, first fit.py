def first_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= processes[i]:
                allocation[i] = j
                memory_blocks[j] -= processes[i]
                break

    return allocation

def worst_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)

    for i in range(len(processes)):
        worst_fit_index = -1
        for j in range(len(memory_blocks)):
            if memory_blocks[j] >= processes[i]:
                if worst_fit_index == -1 or memory_blocks[j] > memory_blocks[worst_fit_index]:
                    worst_fit_index = j

        if worst_fit_index != -1:
            allocation[i] = worst_fit_index
            memory_blocks[worst_fit_index] -= processes[i]

    return allocation

if __name__ == "__main__":
    memory_blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]

    best_fit_allocation = best_fit(memory_blocks.copy(), processes)
    first_fit_allocation = first_fit(memory_blocks.copy(), processes)
    worst_fit_allocation = worst_fit(memory_blocks.copy(), processes)

    print("Best Fit Allocation:", best_fit_allocation)
    print("First Fit Allocation:", first_fit_allocation)
    print("Worst Fit Allocation:", worst_fit_allocation)
