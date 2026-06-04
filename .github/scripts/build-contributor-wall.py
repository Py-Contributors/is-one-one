import json
import re
from pathlib import Path

README = Path("README.md")

# Load contributors from the files
contributors = json.loads(
    Path("/tmp/contributors.json").read_text(encoding="utf-8")
)

cards = []

# It create one contributor card
for c in contributors:
    cards.append(
        f"""
    <a href="{c['html_url']}" style="text-decoration:none;">
        <img
            src="{c['avatar_url']}&s=64"
            width="64"
            height="64"
            alt="{c['login']}"
            style="border-radius:50%; margin:4px;"
        />
        <br/>
        <sub>{c['login']}</sub>
    </a>
    """
    )

# Build contributor wall
wall = f"""
<div align="center">

### {len(contributors)} Contributors

{"\n".join(cards)}

*Auto-updated daily · <a href="https://github.com/itsdakshjain/is-one-one/graphs/contributors">View all →</a>*

</div>
"""

# Read README
content = README.read_text(encoding="utf-8")

# Replace everything between the markers
content = re.sub(
    r"<!-- CONTRIBUTOR-WALL-START -->.*?<!-- CONTRIBUTOR-WALL-END -->",
    f"<!-- CONTRIBUTOR-WALL-START -->\n{wall}\n<!-- CONTRIBUTOR-WALL-END -->",
    content,
    flags=re.S,
)

# Write updated README
README.write_text(content, encoding="utf-8")
