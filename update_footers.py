import os
import re

# Directory containing the HTML files
DIR = "/Users/raman/projects/WeAppTesters"

# Extract the footer from index.html
with open(os.path.join(DIR, "index.html"), "r") as f:
    index_content = f.read()

# Use regex to find the footer block in index.html
footer_match = re.search(r'(<!-- (?:Advanced )?Footer -->.*?</footer>)', index_content, re.DOTALL)
if not footer_match:
    print("Could not find footer in index.html")
    exit(1)

new_footer = footer_match.group(1)

# Files to update
files_to_update = [
    "blog.html",
    "article.html",
    "privacy-policy.html",
    "terms-of-service.html",
    "refund-policy.html"
]

for filename in files_to_update:
    filepath = os.path.join(DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()

        # Find the existing footer and replace it
        # The existing footer might start with <!-- Footer --> or <footer
        updated_content = re.sub(r'<!-- (?:Advanced )?Footer -->.*?</footer>', new_footer, content, flags=re.DOTALL)
        
        # If the comment <!-- Footer --> is missing, just replace from <footer to </footer>
        if updated_content == content:
            updated_content = re.sub(r'<footer.*?</footer>', new_footer, content, flags=re.DOTALL)

        with open(filepath, "w") as f:
            f.write(updated_content)
        print(f"Updated {filename}")
    else:
        print(f"{filename} not found")
