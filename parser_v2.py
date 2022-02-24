import json
from pprint import pprint
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
                #pprint(line)
                line_split = line.split(":")
                decanat[village][line_split[0]] = line_split[1].replace("\n", '')
                pprint(line_split)
                pprint(decanat[village][line_split[0]])


    #write_json(decanat)
    return decanat
def parse_dict(decanat: dict)->dict:
    """
    parses dict
    key -> subkey -> info ->
    parse info
    :param dict decanat:

    :return dict
    
    """
    for village in decanat:
        for village_info in decanat[village]:
            for rubric in village_info:
                pprint(rubric)
                if village_info == "Н":
                    pprint(village_info)
                    pprint(decanat[village][village_info])
                    pprint(decanat[village])
                if rubric == "a":
                    pprint(village_info)
                    pprint(decanat[village][village_info])
                    pprint(decanat[village])
                else:
                    for rubric_info in village_info[rubric]:
                        line_without_semis = rubric_info.split(";")
                        for semi in line_without_semis:
                            line_without_comas = semi.split(",")
                            for info_bit in line_without_comas:
                                info_bit = info_bit.strip("\n")
                                info_bit = info_bit.strip(".")
                                info_bit_split = info_bit.split(" ")
                                if "ha" in info_bit:
                                    building_type_key = info_bit_split[1]
                                    #pprint(building_type_key)
                                    line_index =  info_bit_split.index("ha") - 1
                                    ha = info_bit_split[line_index]
                                    #pprint(ha)
                                    if building_type_key == ha:
                                        building_type_key = "п."
                                if "a" in info_bit:
                                    #building_type_key = info_bit_split[1]
                                    #pprint(building_type_key)
                                    line_index =  info_bit_split.index("a") - 1
                                    a = info_bit_split[line_index]
                                    #pprint(a)
                                if "m2" in info_bit:
                                    #building_type_key = info_bit_split[1]
                                    #pprint(building_type_key)
                                    line_index =  info_bit_split.index("m2") - 1
                                    m2 = info_bit_split[line_index]
                                    #pprint(m2)
                                    #pprint(info_bit)

decanat = parser("file2.txt")
parse_dict(decanat)