import os
import re

DIR = "/Users/raman/projects/WeAppTesters"

# Extract the script and floating button from index.html
with open(os.path.join(DIR, "index.html"), "r") as f:
    index_content = f.read()

# Grab everything from <!-- Interactive Scripts --> to the end of the file (before </body>)
scripts_match = re.search(r'(<!-- Interactive Scripts -->.*?)</body>', index_content, re.DOTALL)
if not scripts_match:
    print("Could not find interactive scripts in index.html")
    exit(1)

new_scripts = scripts_match.group(1)

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

        # Check if <!-- Interactive Scripts --> exists
        if "<!-- Interactive Scripts -->" in content:
            # Replace from <!-- Interactive Scripts --> to </body>
            updated_content = re.sub(r'<!-- Interactive Scripts -->.*?</body>', new_scripts + "\n  </body>", content, flags=re.DOTALL)
        else:
            # Insert before </body>
            updated_content = re.sub(r'</body>', "\n    " + new_scripts + "\n  </body>", content, flags=re.DOTALL)

        with open(filepath, "w") as f:
            f.write(updated_content)
        print(f"Updated scripts in {filename}")
    else:
        print(f"{filename} not found")
