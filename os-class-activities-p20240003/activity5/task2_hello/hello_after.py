#!/usr/bin/env python3
"""
Task 2 - AFTER semaphore version (correct ordering with semaphores)
Three concurrent workers always print HELLO in the correct order.
"""
import threading

# Semaphores to control print order
start_h  = threading.Semaphore(1)  # Process 1 can start immediately
after_e  = threading.Semaphore(0)  # Process 2 waits until HE is printed
after_l1 = threading.Semaphore(0)  # Process 2 waits for its own first L signal
after_l2 = threading.Semaphore(0)  # Process 3 waits until LL is printed

def process1():
    """Prints H and E"""
    start_h.acquire()
    print("H", end="", flush=True)
    print("E", end="", flush=True)
    after_e.release()   # signal Process 2 to print first L

def process2():
    """Prints L and L"""
    after_e.acquire()   # wait for HE
    print("L", end="", flush=True)
    after_l1.release()  # signal self for second L

    after_l1.acquire()
    print("L", end="", flush=True)
    after_l2.release()  # signal Process 3 to print O

def process3():
    """Prints O"""
    after_l2.acquire()  # wait for LL
    print("O", end="", flush=True)

print("=== AFTER semaphore version (correct ordering) ===")
print("Output must always be HELLO:\n")

for attempt in range(5):
    # Reset semaphores for each run
    start_h  = threading.Semaphore(1)
    after_e  = threading.Semaphore(0)
    after_l1 = threading.Semaphore(0)
    after_l2 = threading.Semaphore(0)

    def process1():
        start_h.acquire()
        print("H", end="", flush=True)
        print("E", end="", flush=True)
        after_e.release()

    def process2():
        after_e.acquire()
        print("L", end="", flush=True)
        after_l1.release()
        after_l1.acquire()
        print("L", end="", flush=True)
        after_l2.release()

    def process3():
        after_l2.acquire()
        print("O", end="", flush=True)

    print(f"Attempt {attempt+1}: ", end="", flush=True)
    threads = [
        threading.Thread(target=process1),
        threading.Thread(target=process2),
        threading.Thread(target=process3),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print()

print("\nAll attempts printed HELLO correctly. Program terminated normally.")
