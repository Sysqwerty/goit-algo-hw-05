def read_file_content(src):
    try:
        with open(src, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{src}' not found.")
    except IOError as e:
        print(f"I/O error: {e}")
    except Exception as e:
        print(f"Unknown error: {e}")
    return None  # Return None in case of an exception
