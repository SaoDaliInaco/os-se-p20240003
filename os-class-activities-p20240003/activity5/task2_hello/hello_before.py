#!/usr/bin/env python3
"""
Task 2 - BEFORE semaphore version (no ordering)
Three concurrent workers print letters without coordination.
Output order is unpredictable - may NOT be HELLO.
"""
import threading
import time
import random

def process1():
    time.sleep(random.uniform(0, 0.01))
    print("H", end="", flush=True)
    time.sleep(random.uniform(0, 0.01))
    print("E", end="", flush=True)

def process2():
    time.sleep(random.uniform(0, 0.01))
    print("L", end="", flush=True)
    time.sleep(random.uniform(0, 0.01))
    print("L", end="", flush=True)

def process3():
    time.sleep(random.uniform(0, 0.01))
    print("O", end="", flush=True)

print("=== BEFORE semaphore version (no ordering) ===")
print("Expected: HELLO  |  Actual output may differ:\n")

for attempt in range(5):
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
    print()  # newline after each attempt

print("\nNote: Without semaphores, letters can print in wrong order.")
