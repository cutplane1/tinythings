#include <string.h>
#include <stdio.h>

int check_for_license(char *str)
{
    char cmd[256];
    snprintf(cmd, sizeof(cmd), "curl -s \"http://127.0.0.1:8000/check?key=%s\"", str);

    FILE *fp = popen(cmd, "r");
    if (!fp) return -1; 

    char res[256];
    fgets(res, sizeof(res), fp);
    pclose(fp);

    if (strstr(res, "OK") != NULL)
        return 1;

    return 0;
}

int ask_for_license()
{
    char key[32];
    printf("enter your license key: ");
    scanf("%31s", key);
    int u = check_for_license(key);

    if (u == 0)
    {
        printf("Invalid license key.\n");
        return ask_for_license();
    } else if (u == -1)
    {
        printf("Error checking license key.\n");
        return ask_for_license();
    } else {
        return 0;
    }
}