import java.util.*;

class Process implements Comparable<Process> {
    int id;
    int arrivalTime;
    int burstTime;

    public Process(int id, int arrivalTime, int burstTime) {
        this.id = id;
        this.arrivalTime = arrivalTime;
        this.burstTime = burstTime;
    }

    @Override
    public int compareTo(Process other) {
        return Integer.compare(this.burstTime, other.burstTime);
    }
}

public class SJF{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of processes: ");
        int n = scanner.nextInt();

        List<Process> processes = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            System.out.print("Enter arrival time for process " + i + ": ");
            int arrivalTime = scanner.nextInt();
            System.out.print("Enter burst time for process " + i + ": ");
            int burstTime = scanner.nextInt();
            processes.add(new Process(i, arrivalTime, burstTime));
        }

        Collections.sort(processes, (p1, p2) -> {
            if (p1.arrivalTime == p2.arrivalTime) {
                return Integer.compare(p1.burstTime, p2.burstTime);
            }
            return Integer.compare(p1.arrivalTime, p2.arrivalTime);
        });

        int currentTime = 0;
        double totalWaitTime = 0;
        System.out.println("\nProcess\tArrival Time\tBurst Time\tWait Time\tTurnaround Time");
        for (Process process : processes) {
            if (currentTime < process.arrivalTime) {
                currentTime = process.arrivalTime;
            }
            int waitTime = currentTime - process.arrivalTime;
            int turnaroundTime = waitTime + process.burstTime;
            totalWaitTime += waitTime;
            System.out.println(process.id + "\t\t" + process.arrivalTime + "\t\t" + process.burstTime + "\t\t" + waitTime + "\t\t" + turnaroundTime);
            currentTime += process.burstTime;
        }

        double averageWaitTime = totalWaitTime / n;
        System.out.println("\nAverage Wait Time: " + averageWaitTime);

        scanner.close();
    }
}
