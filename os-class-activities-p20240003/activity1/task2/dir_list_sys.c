#include <fcntl.h>
#include <unistd.h>
#include <dirent.h>
#include <sys/stat.h>
#include <string.h>
#include <stdio.h>   // for snprintf()

int main() {
    char buffer[512];

    // 1. Open current directory
    DIR *dir = opendir(".");
    if (dir == NULL) {
        char *err = "Error opening directory\n";
        write(2, err, strlen(err));
        return 1;
    }

    // 2. Print header
    char *header = "File Name                     Size(bytes)\n";
    write(1, header, strlen(header));

    struct dirent *entry;
    struct stat fileStat;

    // 3. Loop through directory entries
    while ((entry = readdir(dir)) != NULL) {

        // 4. Get file info using stat()
        if (stat(entry->d_name, &fileStat) == 0) {

            // 5. Format output into buffer
            snprintf(buffer, sizeof(buffer),
                     "%-30s %10ld\n",
                     entry->d_name,
                     fileStat.st_size);

            // Write to terminal
            write(1, buffer, strlen(buffer));
        }
    }

    // 6. Close directory
    closedir(dir);

    return 0;
}
