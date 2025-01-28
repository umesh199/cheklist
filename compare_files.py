import os
import json
import filecmp

def load_config(config_path):
    """Load the configuration file containing expected files and their actual paths."""
    with open(config_path, 'r') as file:
        return json.load(file)

def compare_files(expected_dir, file_mapping):
    """Compare the expected files with actual system files."""
    results = []
    
    for filename, actual_path in file_mapping.items():
        expected_path = os.path.join(expected_dir, filename)
        
        if not os.path.exists(expected_path):
            results.append(f"{filename}: Expected file does not exist in {expected_dir} (MISMATCH)")
        elif not os.path.exists(actual_path):
            results.append(f"{filename}: Actual file does not exist at {actual_path} (MISMATCH)")
        elif filecmp.cmp(expected_path, actual_path):
            results.append(f"{filename}: PASS")
        else:
            results.append(f"{filename}: Content mismatch (MISMATCH)")
    
    return results

def main():
    # Paths
    config_path = "./config.json"          # Path to the JSON file
    expected_directory = "./expected"     # Directory where expected files are stored
    
    # Load configurations
    config = load_config(config_path)
    file_mapping = config.get("files", {})
    
    # Compare files
    results = compare_files(expected_directory, file_mapping)
    
    # Print results
    for line in results:
        print(line)

if __name__ == "__main__":
    main()
