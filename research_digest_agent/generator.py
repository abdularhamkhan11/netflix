import os
import json

def generate_outputs(groups, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    # digest.md
    with open(os.path.join(output_folder, "digest.md"), "w", encoding="utf-8") as f:
        f.write("# Research Digest: AI in Healthcare\n\n")

        for i, (theme, claims) in enumerate(groups.items(), 1):
            f.write(f"## Theme {i}\n")

            for c in claims:
                f.write(f"- {c['claim']} ({c['source']})\n")

            f.write("\n")

    # sources.json
    with open(os.path.join(output_folder, "sources.json"), "w", encoding="utf-8") as f:
        json.dump(groups, f, indent=4)