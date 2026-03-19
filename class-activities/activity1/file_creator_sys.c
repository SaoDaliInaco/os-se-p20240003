#include <fcntl.h>    // open()
#include <unistd.h>   // write(), close()
#include <string.h>   // strlen()

int main() {
    // Text to write into file
    char *text = "Hello from Operating Systems class!\n";

    // Open/Create file
    int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);

    // Check if file opened successfully
    if (fd < 0) {
        char *err = "Error creating file\n";
        write(2, err, strlen(err)); // fd 2 = stderr
        return 1;
    }

    // Write to file
    write(fd, text, strlen(text));

    // Close file
    close(fd);

    // Print confirmation to terminal
    char *msg = "File created successfully!\n";
    write(1, msg, strlen(msg)); // fd 1 = stdout

    return 0;
}
