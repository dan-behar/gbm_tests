def extracter(name):
    """
    Function that extracts all the components from the .txt file
    and turns them into arrays of ints ready to be processed
    Inputs:
        - name (str): the name of the file (includes .txt in the name)
    Outputs:
        - clean_data (arr): array of arrays containing all the clean data
    """
    input = []
    clean_data = []
    
    # Read the file
    with open(name) as f:
        for line in f:
            inner_list = [elt.strip() for elt in line.split(' ')]
            input.append(inner_list)

    # Cleaning the file
    for i in range(len(input)):
        arr = [int(numeric_string) for numeric_string in input[i]]
        clean_data.append(arr)
    
    return clean_data

def positions(info):
    """
    Function that calculates all the points that the competitors
    got in the races and with the new tables
    Inputs:
        - info (arr): array of arrays containing all the clean data
    Outputs:
        - carreras (arr): array of arrays containing all the points
            per competitor for each table
    """
    # Indexes that will help me go through the information
    indexes = [i for i in range(len(info)) if len(info[i]) == 2]
    len_1_indexes = [i for i in range(len(info)) if len(info[i]) == 1]
    carreras = []

    # Iterating using all the lists with only 2 elements
    for i in range(len(indexes)):

        # It will go in the document until it reaches the end of the document ending with [0, 0]
        if sum(info[indexes[i]]) > 0:
            num_races = info[indexes[i]][0]
            num_table_points = info[len_1_indexes[i]][0]
            points = [0] * info[indexes[i]][1]

            if num_races == 1:
                for r in range(len_1_indexes[i]+1, len_1_indexes[i]+num_table_points+1): # movements per table point
                    for k in range(len(info[i+1])): # positions per competitor
                        posicion = info[i+1][k]
                        if posicion >= len(info[r]):
                            # If the position doesn't get points, it receives a 0
                            points[k] = 0
                        else:
                            points[k] = points[k] + info[r][posicion]
                    # After it ends all races per table, it saves the results
                    carreras.append(points)
                    points = [0] * info[indexes[i]][1]

            else:
                for r in range(len_1_indexes[i]+1, len_1_indexes[i]+num_table_points+1): ## movements per table point
                    for j in range(indexes[i]+1, indexes[i]+num_races+1): # movements per race (Grand Prix)
                        for k in range(len(info[j])): # positions per competitor
                            posicion = info[j][k]
                            if posicion >= len(info[r]):
                                # If the position doesn't get points, it receives a 0
                                points[k] = 0
                            else:
                                points[k] = points[k] + info[r][posicion]
                    # After it ends all races per table, it saves the results
                    carreras.append(points)
                    points = [0] * info[indexes[i]][1]
        else:
            return carreras
        
def results(res):
    index = ""
    for i in range(len(res)):
        val = max(res[i])
        for j in range(len(res[i])):
            if res[i][j] == val:
                temp = j + 1
                index = index + str(temp) + " "
        index = index + "\n"

    f = open("output.txt", "w")
    f.write(index)
    f.close()
        

# Beginning of the program
print("Ingrese el nombre del archivo de texto asi: nombre.txt")
info = input("Ingrese el nombre del archivo: ")

#Checking that the name of the file meets the requirements
if len(info) >= 4 and info[-4:] == ".txt":
    try:
        res = extracter(info)
        values = positions(res)
        results(values)
    except:
        print("No se ha encontrado el archivo")
        exit()
else:
    print("El nombre del archivo no cuenta con las especificaciones adecuadas")
    exit()