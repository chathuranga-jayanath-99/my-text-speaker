import json 

class TextJson:
    def __init__(self, file_path):
        self.file_path = file_path 

    def read_json(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
            return data 
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return None
    
if __name__ == "__main__":
    filepath = "texts.json"
    json_text_manager = TextJson(filepath)
    json_data = json_text_manager.read_json()
    print(f"data: {json_data}")
    print(f"name: {json_data['name']}")
    # print(f"list: {json_data["texts"]}")