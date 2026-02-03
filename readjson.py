import json
import os

class JSONReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def read_json_file(self):
        """
        Reads data from the specified JSON file into a Python dictionary.
        """
        if not os.path.exists(self.filename):
            print(f"Error: The file '{self.filename}' was not found.")
            return False
        
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
            return True
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file: {e}")
            return False
        except IOError as e:
            print(f"Error reading file: {e}")
            return False

    def get_data(self):
        """
        Returns the loaded data (a Python dictionary or list).
        """
        return self.data

    def get_value(self, key_path, default=None):
        """
        Safely retrieves a nested value using a list of keys (e.g., ['mydata', 'addressBookEntry', 'city']).
        """
        if self.data is None:
            return default
        
        temp_data = self.data
        try:
            for key in key_path:
                temp_data = temp_data[key]
            return temp_data
        except (KeyError, IndexError, TypeError):
            return default