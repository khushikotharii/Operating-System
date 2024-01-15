class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time

def round_robin(processes, quantum):
    time = 0
    queue = []
    waiting_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)
    
    while True:
        for process in processes:
            if process.arrival_time <= time and process.remaining_time > 0:
                if process.remaining_time <= quantum: 
                    time += process.remaining_time
                    waiting_time[processes.index(process)] = time - process.arrival_time - process.burst_time
                    process.remaining_time = 0
                else:
                    time += quantum
                    process.remaining_time -= quantum
                queue.append(process)
        
        if len(queue) == 0:
            break
        
        # Completed process at the end of the queue
        while queue and queue[0].remaining_time == 0:
            queue.pop(0)  # Ensure the queue is not empty before popping
        
    # TAT
    for i in range(len(processes)):
        turnaround_time[i] = processes[i].burst_time + waiting_time[i]
        
    sumturnaroundtime = sum(turnaround_time)
    sumwaitingtime = sum(waiting_time)
    avgturnaroundtime = sumturnaroundtime / len(processes)
    avgwaitingtime = sumwaitingtime / len(processes)
    
    
    
    # Printing Results
    print("Process\tWaiting Time\tTurnaround Time")
    for i in range(len(processes)):
        print(processes[i].name,"\t",waiting_time[i],"\t\t",turnaround_time[i])
    print("Avg TurnAroundTime: ",avgturnaroundtime, "\nAvg WaitingTime: ",avgwaitingtime)

if __name__ == "__main__":
    processes = []
    num_processes = int(input("Enter the number of processes: "))
    
    for i in range(num_processes):
        name = input(f"Enter name for process {i + 1}: ")
        arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        processes.append(Process(name, arrival_time, burst_time))
    
    quantum = int(input("Enter the quantum time slice: "))
    round_robin(processes, quantum)