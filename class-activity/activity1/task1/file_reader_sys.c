#include <fcntl.h>
#include <unistd.h>

int main() {
    char buffer[256];

    // 1. Open file
    int fd = open("output.txt", O_RDONLY);
    if (fd < 0) {
        char *err = "Error opening file\n";
        write(2, err, 20);
        return 1;
    }

    // 2 & 3. Read + display using loop
    int bytesRead;
    while ((bytesRead = read(fd, buffer, sizeof(buffer))) > 0) {
        write(1, buffer, bytesRead);
    }

    // 4. Close file
    close(fd);

    return 0;
}
