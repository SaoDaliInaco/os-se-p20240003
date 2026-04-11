#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int pid = fork();

    if (pid == 0) {
        // Child
        printf("Child (PID %d): I'm done. Exiting now.\n", getpid());
    } else {
        // Parent
        printf("Parent (PID %d): Child PID is %d.\n", getpid(), pid);
        sleep(10);  // wait before cleaning
        wait(NULL); // clean zombie
        printf("Parent: Collected child. Zombie should be gone.\n");
        sleep(10); // keep alive to verify
    }

    return 0;
}
