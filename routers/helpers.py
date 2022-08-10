def filter_by_number(num, data):
    filtered_data = []
    for p in data:
        if str(p["number"]).find(num) != -1:
            filtered_data.append(p)
    return filtered_data

def filter_by_name(name, data):
    filtered_data = []
    for p in data:
        if p["name"].lower().find(name.lower()) != -1:
            filtered_data.append(p)
    return filtered_data

def filter_by_types(types, data):
    filtered_data = []
    number_of_types = len(types)
    for p in data:
        matched_types = 0
        for t in types:
            if t in p["type"]:
                matched_types += 1
        if matched_types == number_of_types:
            filtered_data.append(p)
    return filtered_data

def filter_by_weaknesses(weaknesses, data):
    filtered_data = []
    number_of_weaknesses = len(weaknesses)
    for p in data:
        matched_types = 0
        for w in weaknesses:
            if w in p["weaknesses"]:
                matched_types += 1
        if matched_types == number_of_weaknesses:
            filtered_data.append(p)
    return filtered_data

def filter_by_ability(ability, data):
    filtered_data = []
    for p in data:
        isMatch = False
        for a in p["info"][4]["value"]:
            if a["name"].lower() == ability.lower():
                isMatch = True
        if isMatch:
            filtered_data.append(p)
    return filtered_data

def filter_by_heights(heights, data):
    filtered_data = []
    for p in data:
        p_height = int(p["info"][0]["value"].split("'")[0])
        if "small" in heights:
            if p_height < 4:
                filtered_data.append(p)
        if "medium" in heights:
            if (p_height < 7) & (p_height >= 4):
                filtered_data.append(p)
        if "large" in heights:
            if p_height >= 7:
                filtered_data.append(p)
    return filtered_data

def filter_by_weights(weights, data):
    filtered_data = []
    for p in data:
        p_weight = float(p["info"][1]["value"].split()[0])
        if "small" in weights:
            if p_weight < 90:
                filtered_data.append(p)
        if "medium" in weights:
            if (p_weight < 500) & (p_weight >= 90):
                filtered_data.append(p)
        if "large" in weights:
            if p_weight >= 500:
                filtered_data.append(p)
    return filtered_data


