import re

# PHI values to search for
first_name = 'jane'
last_name = 'doe'
mrn = '12345678'

pattern_type = '[^\s]*'

# Compile regex patterns
patterns = {
    'first_name': re.compile(rf'{pattern_type}{re.escape(first_name)}{pattern_type}', re.IGNORECASE),
    'last_name': re.compile(rf'{pattern_type}{re.escape(last_name)}{pattern_type}', re.IGNORECASE),
    'mrn': re.compile(rf'{pattern_type}{re.escape(mrn)}{pattern_type}')
}

# Function to find PHI
def find_phi_matches(text):
    matches = {}
    for key, pattern in patterns.items():
        found = pattern.findall(text)
        if found:
            matches[key] = found
    return matches

# Optional: Function to redact PHI
def redact_phi(text):
    redacted = text
    for key, pattern in patterns.items():
        replacement_text = f'REDACTED_{key.upper()}'
        redacted = pattern.sub(f"*******", redacted)
    return redacted

# 🔢 Example strings to process
texts = [
    "Patient Jane Doe, MRN: 12345678, is stable.",
    "Nothing to see here.",
    "MRN: 12345678 is assigned to Jane, last name unknown.",
    "JANE DOE was admitted. MRN is 12345678.",
    "janedoe12345678 should not be matched as valid PHI.",
    "MRN 12345678. Another Jane reported dizziness.",
    "Usernames: janedoe@, jane, Maryjane, notjane123, ?jane?, @jane#, #jdoe",
    "Codes in #12345678 M1234567891, check"
]

# 🚀 Process each text
for i, text in enumerate(texts, 1):
    print(f"\n--- Text {i} ---")
    print("Original:", text)

    matches = find_phi_matches(text)
    if matches:
        print("PHI matches found:", matches)
    else:
        print("No PHI matches.")

    redacted_text = redact_phi(text)
    print("Redacted:", redacted_text)

assert True
