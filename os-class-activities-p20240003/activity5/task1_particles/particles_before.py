#!/usr/bin/env python3
"""
Task 1 - BEFORE semaphore version (intentionally unsafe)
No synchronization -> race conditions -> errors occur
"""
import threading
import time
import random

BUFFER_CAPACITY = 100  # max particles
buffer = []
produced_count = 0
packaged_count = 0
running = True

# NO locks, NO semaphores - intentionally unsafe

def producer(machine_id):
    global produced_count, running
    pair_id = 0
    while running:
        pair_id += 1
        p1 = f"M{machine_id}-{pair_id}-P1"
        p2 = f"M{machine_id}-{pair_id}-P2"

        # UNSAFE: no check before adding - can exceed capacity
        if len(buffer) + 2 > BUFFER_CAPACITY:
            print("The producing machine is broken")
            running = False
            return

        # Simulate a context switch gap between adding P1 and P2
        buffer.append(p1)
        time.sleep(random.uniform(0, 0.001))  # context switch window
        buffer.append(p2)

        produced_count += 1
        time.sleep(random.uniform(0.001, 0.005))


def consumer():
    global packaged_count, running
    while running:
        # UNSAFE: no check before removing
        if len(buffer) == 0:
            print("The packaging machine is broken")
            running = False
            return

        if len(buffer) < 2:
            time.sleep(0.001)
            continue

        # UNSAFE: another thread may have modified buffer between checks
        item1 = buffer.pop(0)
        time.sleep(random.uniform(0, 0.001))  # context switch window
        if len(buffer) == 0:
            print("The packaging machine is broken")
            running = False
            return
        item2 = buffer.pop(0)

        # Verify pair
        # Format: M<machine>-<pair_id>-P1 / M<machine>-<pair_id>-P2
        prefix1 = "-".join(item1.split("-")[:2])
        prefix2 = "-".join(item2.split("-")[:2])

        if prefix1 != prefix2:
            print(f"Pairs are incorrect")
            print(f"  Got: {item1} + {item2}")
            running = False
            return

        packaged_count += 1
        buf_size = len(buffer)
        print(f"Produced pairs: {produced_count} | Packaged pairs: {packaged_count} | Buffer particles: {buf_size}")
        time.sleep(random.uniform(0.001, 0.003))


# Start 3 producers and 1 consumer (no synchronization)
threads = []
for i in range(1, 4):
    t = threading.Thread(target=producer, args=(i,), daemon=True)
    threads.append(t)

c = threading.Thread(target=consumer, daemon=True)
threads.append(c)

print("=== BEFORE semaphore version (unsafe) ===")
print("Expect errors due to race conditions...\n")

for t in threads:
    t.start()

for t in threads:
    t.join(timeout=10)

print("\nProgram ended.")
