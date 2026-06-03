import json
import re
from pathlib import Path

README = Path("README.md")

# load contributors data from file
contributors = json.loads(
    Path("/tmp/contributors.json").read_text(encoding="utf-8")
)

cards = []

# It creates card for each contibutor
for c in contributors:
    cards.append(
        f'''<td align="center">
<a href="{c["html_url"]}">
<img src="{c["avatar_url"]}&s=64" width="52" height="52" alt="{c["login"]}"
style="border-radius:50%;margin:4px"/><br/>
<sub><b>{c["login"]}</b></sub><br/>
<sub>{c["contributions"]} commits</sub>
</a>
</td>'''
    )

rows = []

# It creates rows of 12 cards each
for i in range(0, len(cards), 12):
    rows.append("<tr>" + "".join(cards[i:i+12]) + "</tr>")

wall = f"""
<div align="center">

### {len(contributors)} Contributors

<table>
{''.join(rows)}
</table>

*Auto-updated daily · <a href="https://github.com/Py-Contributors/is-one-one/graphs/contributors">View all →</a>*  # noqa: E501

</div>
"""

# read the content of README.md
content = README.read_text(encoding="utf-8")

# replace the content with new contribotr wall between markers
content = re.sub(
    r"<!-- CONTRIBUTOR-WALL-START -->.*?<!-- CONTRIBUTOR-WALL-END -->",
    f"<!-- CONTRIBUTOR-WALL-START -->\n{wall}\n<!-- CONTRIBUTOR-WALL-END -->",
    content,
    flags=re.S,
)

# Write the updated content back to README.md
README.write_text(content, encoding="utf-8")
