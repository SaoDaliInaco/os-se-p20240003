# Class Activity 6 - Deadlock Simulation

- **Student Name:** Sao Dali Inaco
- **Student ID:** p20240003
- **Programming Language Used:** java

---

## Task 1: Deadlock Version

![Deadlock version](screenshots/task1_deadlock.png)

- Shared resources:
- Transaction 1:
- Transaction 2:
- Deadlock message shown:
- Explanation of why the program got stuck:

---

## Task 2: Deadlock Prevention Version

![Deadlock prevention](screenshots/task2_prevention.png)

- Prevention strategy used:
- Semaphore mutex initial value:
- Starting total:
- Final total:
- Did both transfers complete?
- Why no deadlock occurred:

---

## Questions

1. What are the two shared resources in your bank transaction simulation?
> The two shared resources are Account-A and Account-B. Each account has a semaphore lock that both threads must access during money transfers.

2. Which line or section of your Task 1 program creates hold-and-wait?
> from.lock.acquire(); - to.lock.acquire();

3. How does Task 1 create circular wait?
> Each thread is waiting for a resource held by the other thread, forming a circular dependency.

4. Why does the Task 1 program need a watchdog or timeout?
> A deadlocked program can wait forever without producing further output. The watchdog detects when the threads remain blocked for too long and reports the deadlock instead of letting the program hang indefinitely
.
5. How does the single semaphore mutex prevent deadlock in Task 2?
> The single semaphore mutex allows only one thread to perform a transfer at a time. Since a thread must acquire the mutex before accessing any account, no other thread can hold a conflicting resource simultaneously. This removes the possibility of threads waiting on each other.

6. Which of the four deadlock conditions does your Task 2 solution remove or avoid?
> A thread must acquire the single mutex before performing any transfer, so it never holds one resource while waiting for another. Without hold-and-wait, deadlock cannot occur.

7. Why must the final total bank balance remain unchanged after both transfers?
> Money is only moved between accounts; no money is created or destroyed.

---

## Reflection

_What did this activity teach you about deadlock prevention in real systems such as banking, databases, or file systems?_
