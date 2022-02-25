import json
def write_json(dictionary):
    with open("dict.json", "w", encoding= " utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent= 4)
        
def parser(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    decanat = {}
    for line in lines:
        if len(line) > 1:
            if ")" in line[1]:
                split_line = line[3:].split(",")
                village = split_line[0]
                decanat[village] = {}
            elif ")" in line[2]:
                split_line = line[4:].split(",")
                village = split_line[0]
                decanat[village] = {}
            else:
                print(line)
                line_split = line.split(":")
                decanat[village][line_split[0]] = line_split[1].replace("\n", '')

    write_json(decanat)
    print(decanat)

parser("file2.txt")
