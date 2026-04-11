#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    for (int i = 0; i < 3; i++) {
        int pid = fork();

        if (pid == 0) {
            printf("Child %d (PID %d) running\n", i+1, getpid());
            sleep(30); // keep alive for observation
            return 0;
        }
    }

    // Parent waits for all children
    for (int i = 0; i < 3; i++) {
        wait(NULL);
    }

    printf("Parent: All children finished.\n");
    return 0;
}
