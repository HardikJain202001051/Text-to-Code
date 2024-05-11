import json

import re
from tqdm import tqdm
def is_react_code(js_code):
    # Regular expression to search for React imports or JSX syntax
    react_pattern = r'<\s*[a-zA-Z]+[^>]*\s*\/\s*>'
    if re.search(react_pattern, js_code) or 'React' in  js_code or 'react' in js_code:
        return True
    return False

def check_js_files(json_file):
    rornot = {'1':[],'0':[]}
    try:
        with open(json_file, 'r') as f:
            js_data = json.load(f)
            for file_name, code in tqdm(js_data.items()):
                if is_react_code(code):
                    rornot['1'].append(file_name)
                else:
                    rornot['0'].append(file_name)
        with open('does_contain_react_or_not.json', 'w', encoding='UTF-8') as f:
            json.dump(rornot,f,indent=4)
    except FileNotFoundError:
        print("File not found.")

# Replace 'your_json_file.json' with the path to your JSON file
check_js_files('all_files_data.json')
