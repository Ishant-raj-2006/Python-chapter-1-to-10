# Write a programme to generate multiplication tab from 2 to 20 And write Different file Place this file In a folder for a 13 year old

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"table_{n}.txt", "w") as f:
        f.write(table)


for i in range(2,21):
    generateTable(i)