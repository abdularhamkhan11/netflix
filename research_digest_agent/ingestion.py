import os

def read_files(folder_path):
    documents = []

    for file in os.listdir(folder_path):
        path = os.path.join(folder_path, file)

        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()

                if not text:
                    continue

                documents.append({
                    "source": file,
                    "text": text,
                    "length": len(text)
                })

        except Exception as e:
            print(f"Error reading {file}: {e}")

    return documents