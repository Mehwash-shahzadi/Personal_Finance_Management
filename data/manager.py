import json
import os
import shutil
class DataManager:
    _instance=None
    _file_path = "data/data.json"
    _backup_path = "data/backup_data.json"
    def __init__(self):
        self.data_store = {
        "goals": [],
        "alerts": [],
        "projections": [],
        "notifications": []
        }
    @classmethod 
    def get_instance(cls):
        if cls._instance is None:
            cls._instance=DataManager()
        return cls._instance
    
    def load_from_file(self):
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as file:
                try:
                    self.data_store = json.load(file)
                    print("Data loaded successfully.")
                except json.JSONDecodeError:
                    print(" Error decoding JSON. File might be corrupted.")
        else:
            print(" No existing data file found.")

    def save_to_file(self):
        os.makedirs("data", exist_ok=True)
        with open(self._file_path, 'w') as file:
            json.dump(self.data_store, file, indent=4)
            print(" Data saved successfully.")

    def create_backup(self):
        if os.path.exists(self._file_path):
            shutil.copy(self._file_path, self._backup_path)
            print(" Backup created.")
        else:
            print(" No data file to back up.")

    
    def validate_data(self):
        required_keys = ["goals", "alerts", "projections", "notifications"]
        for key in required_keys:
            if key not in self.data_store:
                self.data_store[key] = []
        print(" Data validated.")

    def export_data(self, export_path):
        with open(export_path, 'w') as file:
            json.dump(self.data_store, file, indent=4)
            print(f" Data exported to {export_path}.")

    def import_data(self, import_path):
        if os.path.exists(import_path):
            with open(import_path, 'r') as file:
                try:
                    imported_data = json.load(file)
                    self.data_store.update(imported_data)
                    print(f"Data imported from {import_path}.")
                except json.JSONDecodeError:
                    print("Import failed. Invalid JSON.")
        else:
            print("Import file not found.")

    def add_goal(self, goal):
        self.data_store["goals"].append(goal)

    def add_alert(self, alert):
        self.data_store["alerts"].append(alert)

    def add_projection(self, projection):
        self.data_store["projections"].append(projection)

    def add_notification(self, notification):
        self.data_store["notifications"].append(notification)

    def get_all_data(self):
        return self.data_store






