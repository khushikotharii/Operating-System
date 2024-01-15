import multiprocessing
import queue
a = 10
b = 20

# class Semaphore:
#     def __init__(self, value =1):
#         self.value = value
#         self.queue = queue.Queue()
    
#     def wait(self):
#         if self.value == 1:
#             self.value = 0
#         else:
#             self.queue.put(None)
#             self.queue.wait()
    
#     def signal(self):
#         if not self.queue.empty():
#             self.queue.get()
#         else:
#             self.value=1


# def addition(semaphore):
#     semaphore.wait()
#     global a,b
#     sum = a+b
#     print("Sum = ", sum)
#     semaphore.signal()


# if __name__ == "__main__":
#     semaphore = Semaphore()
#     process1 = Process(target=addition,args=(semaphore,))
#     process2 = Process(target=addition,args=(semaphore,))

#     process1.start()
#     process2.start()

#     process1.join()
#     process2.join()

#     # pool = Pool(processes=2)

#     # pool.apply_async(addition, (semaphore,))
#     # pool.apply_async(addition, (semaphore,))

#     # pool.close()
#     # pool.join()



binary_semaphore = multiprocessing.Lock()
shared_variable = multiprocessing.Value('i', 0)

#Process 1
def process_1(shared_variable, semaphore, turn):
    print("Process 1: Waiting to enter critical section")
    
    # Request entry by putting its turn in the queue
    turn.put(1)
    
    # Busy-wait until it's Process 1's turn
    while turn.empty() or turn.get() != 1:
        pass
    
    with semaphore:
        print("Process 1: Entered critical section")
        shared_variable.value += 1  
        
        # Critical Section
        global a,b
        sum = a + b
        print("Sum: ",sum)

        print(f"Process 1: Updated shared_variable = {shared_variable.value}")
    
    # Remove its turn from the queue
    turn.get()
    
    print("Process 1: Exited critical section")


#Process 2
def process_2(shared_variable, semaphore, turn):
    print("Process 2: Waiting to enter critical section")
    
    # Request entry by putting its turn in the queue
    turn.put(2)
    
    # Busy-wait until it's Process 2's turn
    while turn.empty() or turn.get() != 2:
        pass
    
    with semaphore:
        print("Process 2: Entered critical section")
        shared_variable.value += 2 
        global a,b
        diff = a-b
        print("Difference: ",diff)
        print(f"Process 2: Updated shared_variable = {shared_variable.value}")
    
    # Remove its turn from the queue
    turn.get()
    
    print("Process 2: Exited critical section")


# Create a queue for process turns
turn_queue = multiprocessing.Queue()

# Create two processes
process1 = multiprocessing.Process(target=process_1, args=(shared_variable, binary_semaphore, turn_queue))
process2 = multiprocessing.Process(target=process_2, args=(shared_variable, binary_semaphore, turn_queue))

# Start the processes
process1.start()
process2.start()

# Wait for both processes to finish
process1.join()
process2.join()

print(f"Final value of shared_variable = {shared_variable.value}")
