// https://en.wikipedia.org/wiki/Netpbm

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "mtwister.h"

int main(int argc, char *argv[])
{
    if (argc != 3)
    {
        printf("usage: %s <amount_of_frames> <canvas_resolution>\n", argv[0]);
        printf("example: %s 10 100x100\n", argv[0]);
        return 1;
    }

    int amount = atoi(argv[1]);
    long rows = 0, cols = 0, n = 0;

    if (sscanf(argv[2], "%ldx%ld", &rows, &cols) == 2)
    {
        n = rows * cols;
    }
    else
    {
        printf("err: unparsable resolution");
        printf("usage: %s <amount_of_frames> <canvas_resolution>\n", argv[0]);
        printf("example: %s 10 100x100\n", argv[0]);
        return 1;
    }

    for (int i = 0; i < amount; i++) {
        char filename[100];
        snprintf(filename, 100, "frames/%d.pbm", i);
        FILE *file = fopen(filename, "w");
        if (file == NULL)
        {
            printf("create a directory named frames");
            return 1;
        }
        fprintf(file, "P1\n%d %d\n", rows, cols); // header
        // srand(time(NULL));
        // MTRand r = seedRand(1337);
        MTRand r = seedRand((uint32_t)time(NULL) ^ (uint32_t)getpid());

        // for (long i = 0; i < n; i++)
        // {
        //     // int bit = rand() % 2;
        //     int bit = genRandLong(&r) & 1U;
        //     fprintf(file, "%d ", bit);
        // }
        for (long y = 0; y < rows; y++) {
            for (long x = 0; x < cols; x++) {
                int bit = genRandLong(&r) & 1U;
                fprintf(file, "%d ", bit);
            }
            fprintf(file, "\n");
        }

        fclose(file);
        printf("generated %ld random bits in '%s'\n", n, filename);
    }
    return 0;
}