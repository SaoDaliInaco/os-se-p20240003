#!/usr/bin/env python3
"""
Task 1 - AFTER semaphore version (safe with semaphores)
Uses semaphores to protect the shared buffer correctly.
Run until Ctrl+C.
"""
import threading
import time
import random

BUFFER_CAPACITY = 100       # max particles = 50 pairs
MAX_PAIRS = BUFFER_CAPACITY // 2

buffer = []
produced_count = 0
packaged_count = 0
running = True

# Semaphores
empty_pairs = threading.Semaphore(MAX_PAIRS)   # 50: pair spaces available
full_pairs  = threading.Semaphore(0)            # 0:  completed pairs ready
mutex       = threading.Semaphore(1)            # 1:  protects buffer access


def producer(machine_id):
    global produced_count, running
    pair_id = 0
    while running:
        pair_id += 1
        p1 = f"M{machine_id}-{pair_id}-P1"
        p2 = f"M{machine_id}-{pair_id}-P2"

        time.sleep(random.uniform(0.002, 0.008))  # simulate production time

        empty_pairs.acquire()   # wait for space for one pair
        mutex.acquire()         # lock buffer

        # Safety check (should never trigger with correct semaphores)
        if len(buffer) + 2 > BUFFER_CAPACITY:
            print("The producing machine is broken")
            running = False
            mutex.release()
            return

        buffer.append(p1)
        buffer.append(p2)
        produced_count += 1

        mutex.release()
        full_pairs.release()    # signal one pair is ready


def consumer():
    global packaged_count, running
    while running:
        full_pairs.acquire()    # wait for a complete pair
        mutex.acquire()         # lock buffer

        # Safety check
        if len(buffer) < 2:
            print("The packaging machine is broken")
            running = False
            mutex.release()
            return

        item1 = buffer.pop(0)
        item2 = buffer.pop(0)

        # Verify same pair
        prefix1 = "-".join(item1.split("-")[:2])
        prefix2 = "-".join(item2.split("-")[:2])

        if prefix1 != prefix2:
            print(f"Pairs are incorrect")
            print(f"  Got: {item1} + {item2}")
            running = False
            mutex.release()
            return

        packaged_count += 1
        buf_size = len(buffer)

        mutex.release()
        empty_pairs.release()   # signal one pair slot is free

        print(f"Produced pairs: {produced_count} | Packaged pairs: {packaged_count} | Buffer particles: {buf_size}")
        time.sleep(random.uniform(0.001, 0.004))


print("=== AFTER semaphore version (safe) ===")
print("Running... press Ctrl+C to stop.\n")

threads = []
for i in range(1, 4):  # 3 producer threads
    t = threading.Thread(target=producer, args=(i,), daemon=True)
    threads.append(t)

c = threading.Thread(target=consumer, daemon=True)
threads.append(c)

for t in threads:
    t.start()

try:
    while running:
        time.sleep(0.5)
except KeyboardInterrupt:
    running = False
    print("\nStopped by user (Ctrl+C). No errors detected.")
