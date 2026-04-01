def group_claims(all_claims):
    groups = {}

    for item in all_claims:
        claim = item["claim"]

        key = claim[:40]  # simple grouping

        if key not in groups:
            groups[key] = []

        groups[key].append(item)

    return groups