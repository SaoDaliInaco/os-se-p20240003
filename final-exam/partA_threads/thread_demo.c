#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_THREADS 5

void *worker(void *arg) {
    long id = (long)arg;
    long val = id * id;
    printf("Worker thread %ld (tid=%lu) computed value: %ld\n", id, pthread_self(), val);
    
    long *result = malloc(sizeof(long));
    *result = val;
    pthread_exit((void *)result);
}

int main() {
    pthread_t threads[NUM_THREADS];
    long sum = 0;

    for (long i = 0; i < NUM_THREADS; i++)
        pthread_create(&threads[i], NULL, worker, (void *)i);

    for (int i = 0; i < NUM_THREADS; i++) {
        void *ret;
        pthread_join(threads[i], &ret);
        sum += *(long *)ret;
        free(ret);
    }

    printf("Summary: %d workers joined, total = %ld\n", NUM_THREADS, sum);
    
    return 0;
}

