import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(file: str, delimiter: str = ",", new_line: str = "\n") -> list[dict]:
    with open(file, "rt") as f:
        lists = [i.split(delimiter) for i in f.read().split(new_line) if i]
        headers1 = lists[0]
        value = lists[1:]
        output_list = []
        for line in value:
            output_list.append({headers1[i]: value for i, value in enumerate(line)})
        return output_list

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))