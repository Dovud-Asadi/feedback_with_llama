import os
import json

names = ['first', 'second', 'third', 'fourth', 'fifth']

for i in range(len(names)):
    txt_folder = f'/home/ravshan/speaklish_data_prep/feedback_with_llama/unzipped_folder/data_new_filtered/folder_{i+1}' 
    json_file_path = f'{names[i]}_feedback_responses.json'  

    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as json_file:
            json_data = json.load(json_file)

        json_sessions = set(item['session'] for item in json_data)
        counter = 0
        for filename in os.listdir(txt_folder):
            if filename.endswith('.txt') and filename.startswith('session_'):
                session_number = filename.replace('session_', '').replace('.txt', '')
                
                if session_number in json_sessions:
                    file_path = os.path.join(txt_folder, filename)
                    os.remove(file_path)
                    print(f'Deleted: {file_path}')
                    counter += 1
        
        print(f"Total files deleted in {txt_folder}: {counter}")
    else:
        print(f"JSON file not found: {json_file_path}")
