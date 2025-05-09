import re

import common_usage_words

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

def redact_phi_conditional(text):
    redacted = text
    for key, pattern in patterns.items():
        redacted = pattern.sub(lambda match: replacement_if_needed(match, key), redacted)
    return redacted

def replacement_if_needed(match, key):
    matched_text = match.group()
    if should_redact(matched_text, key):
        return f'REDACTED_{key.upper()}'
    else:
        return matched_text

def should_redact(text, key):
    # Customize this logic as needed
    #Case 1 : Exactly same match words like Na or Da
    if text == key :
        return True

    to_be_redacted = common_usage_words.filter_words_result(text)
    return to_be_redacted

    # return len(text) > 3 and text.lower() not in {'sam', 'joe', 'test'}



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
