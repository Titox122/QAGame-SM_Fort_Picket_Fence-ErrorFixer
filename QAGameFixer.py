import os

def search_uassets_as_text(root_directory, keywords, results_file):
    found_files = []

    for root, _, files in os.walk(root_directory):
        for file in files:
            if file.endswith(".uasset"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file_content:
                        content = file_content.read()
                        if any(keyword in content for keyword in keywords):
                            found_files.append(file_path)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    with open(results_file, 'w', encoding='utf-8') as results:
        results.write("Files containing the specified keywords:\n\n")
        for file in found_files:
            results.write(file + "\n")
    
    print(f"Search completed. {len(found_files)} files found.")
    print(f"Results saved in: {results_file}")


root_directory = "D:\\Projects\\Assets"
keywords = [
    "LD_Assets_Zombie_TB",
    "SM_Fort_Picket_Fence",
    "LD_Assets_Zombie_TB.SM.SM_Fort_Picket_Fence"
]
results_file = "found_results.txt"

search_uassets_as_text(root_directory, keywords, results_file)
