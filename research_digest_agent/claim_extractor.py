def extract_claims(text):
    sentences = text.split(".")
    claims = []

    for s in sentences:
        s = s.strip()

        if len(s) > 30:
            claims.append({
                "claim": s,
                "evidence": s
            })

    return claims[:5]