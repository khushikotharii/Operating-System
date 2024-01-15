import threading
import queue
import time

n = int(input("Enter the number of processes that the buffer can hold: "))
shared_queue = queue.Queue() 
mutex = threading.Semaphore(1)
full = threading.Semaphore(0)   
empty = threading.Semaphore(n) 

class Producer(threading.Thread):
    def run(self):
        global shared_queue, mutex, full, empty
        for i in range(n):
            item = str(i+1)
            empty.acquire()  # Decrements the empty semaphore
            mutex.acquire()  #Sets mutex = 0
            shared_queue.put(item)
            print("Producer Produced: ", item)
            mutex.release()  # Increment mutex
            full.release()   # Increment the full semaphore
            time.sleep(3)

# Define a consumer thread
class Consumer(threading.Thread):
    def run(self):
        global shared_queue, mutex, full, empty
        while True:
            full.acquire()   # Decrements the full semaphore
            mutex.acquire()  # Sets mutex = 0
            if not shared_queue.empty():
                item = shared_queue.get()
                print("Consumed:", item)
                mutex.release()  # Increament mutex
                empty.release()  # Increment the empty semaphore
                time.sleep(0) #Consumer slower than producer, should incur overflow condition and make the producer wait
            else:
                mutex.release()  # Release the mutex
                break


producer_thread = Producer()
consumer_thread = Consumer()
producer_thread.start()
consumer_thread.start()
