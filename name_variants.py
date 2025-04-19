def generate_name_variants(first_name, last_name):
    first = first_name.lower()
    last = last_name.lower()
    first_name_len = len(first)
    last_name_len = len(last)

    first_name_abbreviate_len = first_name_len//2
    if first_name_abbreviate_len < 4 :
        first_name_abbreviate_len = 4

    last_name_abbreviate_len = last_name_len // 2
    if last_name_abbreviate_len < 4:
        last_name_abbreviate_len = 4

    first_initial = first[:first_name_abbreviate_len]
    last_initial = last[:last_name_abbreviate_len]

    variants = set()

    # Full names
    variants.update([first, last, f"{first} {last}", f"{last} {first}"])

    # Initials
    variants.update([
        first_initial,
        last_initial,
        first_initial + last_initial,
        f"{first_initial}.{last_initial}",
        f"{first_initial}_{last_initial}",
        f"{first_initial}-{last_initial}",
    ])

    # Combined forms
    variants.update([
        f"{first}{last}",
        f"{last}{first}",
        f"{first}_{last}",
        f"{last}_{first}",
        f"{first}-{last}",
        f"{last}-{first}",
        f"{first}.{last}",
        f"{last}.{first}",
    ])

    # Abbreviations
    variants.update([
        f"{first[:3]}{last[:3]}",
        # f"{first[:2]}{last[:2]}",
        f"{first_initial}{last}",
        f"{last_initial}{first}",
        f"{first}{last_initial}",
        f"{last}{first_initial}",
    ])

    # Email-style
    variants.update([
        f"{first}.{last}",
        f"{first[0]}{last}",
        f"{first}{last[0]}",
        f"{first}_{last}",
        f"{first}-{last}",
    ])

    return sorted(variants)

perms = generate_name_variants("Jonathan", "Kleen")
for p in perms:
    print(p)

assert True
