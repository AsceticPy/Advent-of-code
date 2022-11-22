#include <stdio.h>
#include <stdlib.h>
#define MAX 50

int main(int argc, char *argv[]){
    char line[MAX] = "";
    int n_line = 0;
    FILE* file = NULL;

    file = fopen("data.txt", "r");

    if (file == NULL)
    {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }
    n_line = count_line(file);
    int value[n_line];
    get_file_value(file, value);

    for (int i = 0; i < n_line; i++){
        for (int n = 0; n < n_line; n++){
            if (i != n && (value[i] + value[n] == 2020)){
                printf("%d\n", (value[i] * value[n]));
                return 0;
            }
        }
    }
    fclose(file);
    printf("No solution was found\n.");
    return 0;

}

int count_line(FILE* file){
    int n_line = 0;
    char line[MAX] = "";
    rewind(file);
    while (fgets(line, MAX, file) != NULL)
    {
        n_line++;
    }
    return n_line;
}

void get_file_value(FILE* file, int *arr){
    //Method for get value line by line and convert string to integer
    char line[MAX] = "";
    int i = 0;
    int value;
    char str[20];
    
    rewind(file);
    while (fgets(line, MAX, file) != NULL)
    {
        strcpy(str,line);
        arr[i] = atoi(str);
        i++;
    }
}