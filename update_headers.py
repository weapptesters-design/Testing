import os
import re

DIR = "/Users/raman/projects/WeAppTesters"

# Extract the header from index.html
with open(os.path.join(DIR, "index.html"), "r") as f:
    index_content = f.read()

header_match = re.search(r'(<!-- Navigation -->.*?<nav.*?id="navbar".*?</nav>)', index_content, re.DOTALL)
if not header_match:
    print("Could not find header in index.html")
    exit(1)

new_header = header_match.group(1)

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

        # Find existing nav and replace it
        # Sometimes there's <!-- Navigation -->, sometimes just <nav id="navbar"
        # We'll regex replace from <!-- Navigation --> to </nav>, OR <nav id="navbar" to </nav>
        
        updated_content = re.sub(r'<!-- Navigation -->.*?<nav.*?id="navbar".*?</nav>', new_header, content, flags=re.DOTALL)
        if updated_content == content:
            updated_content = re.sub(r'<nav.*?id="navbar".*?</nav>', new_header, content, flags=re.DOTALL)
            
        with open(filepath, "w") as f:
            f.write(updated_content)
        print(f"Updated header in {filename}")
    else:
        print(f"{filename} not found")
