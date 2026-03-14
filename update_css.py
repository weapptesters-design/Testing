import os
import re

DIR = "/Users/raman/projects/WeAppTesters"

missing_css = """
      /* Shimmer Effect */
      .btn-shimmer {
        background: linear-gradient(
          110deg,
          #a3e635 20%,
          #ecfccb 30%,
          #a3e635 40%
        );
        background-size: 200% auto;
        animation: shimmer 4s linear infinite;
      }
      @keyframes shimmer {
        to {
          background-position: -200% center;
        }
      }
"""

files_to_update = [
    "privacy-policy.html",
    "terms-of-service.html",
    "refund-policy.html"
]

for filename in files_to_update:
    filepath = os.path.join(DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()

        # If .btn-shimmer is already there, skip
        if ".btn-shimmer" not in content:
            # Insert before </style>
            updated_content = re.sub(r'</style>', missing_css + "    </style>", content)
            
            with open(filepath, "w") as f:
                f.write(updated_content)
            print(f"Added CSS to {filename}")
        else:
            print(f"CSS already exists in {filename}")
    else:
        print(f"{filename} not found")
