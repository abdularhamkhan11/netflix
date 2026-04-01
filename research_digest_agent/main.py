from ingestion import read_files
from claim_extractor import extract_claims
from grouper import group_claims
from generator import generate_outputs

def main():
    print("🚀 Running Research Digest Agent...")

    docs = read_files("data")

    if not docs:
        print("❌ No valid data found in 'data' folder")
        return

    all_claims = []

    for doc in docs:
        claims = extract_claims(doc["text"])

        for c in claims:
            c["source"] = doc["source"]
            all_claims.append(c)

    groups = group_claims(all_claims)

    generate_outputs(groups, "output")

    print("✅ Done! Check 'output' folder")

if __name__ == "__main__":
    main()