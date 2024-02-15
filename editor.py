import os

def read_mindattributes(file_path=".mindattributes"):
    allowed_files = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):  # Ignore empty lines and comments
                    allowed_files.append(line)
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. No files allowed by default.")
    return allowed_files

def is_allowed_file(file_path, allowed_files):
    for allowed_file in allowed_files:
        if file_path.startswith(allowed_file):
            return True
    return False

def create_or_edit_file(file_path, allowed_files):
    if is_allowed_file(file_path, allowed_files):
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                pass  # Creating an empty file
        else:
            # Opening the file for editing
            os.system(f"${os.environ.get('EDITOR', 'vi')} {file_path}")
    else:
        print("You are not allowed to edit or create this file.")

if __name__ == "__main__":
    allowed_files = read_mindattributes()
    file_path = input("Enter the file path you want to edit or create: ")
    create_or_edit_file(file_path, allowed_files)
