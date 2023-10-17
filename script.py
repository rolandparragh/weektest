import datetime

# Calculate the current week
current_week = datetime.date.today().isocalendar()[1]

# Initialize the Markdown content
markdown_content = f"""\
| Week | Name | Contact details |
| ---- | ---- | --------------- |
"""

# Loop through the weeks (1 to 52)
for week in range(1, 53):
    if week == current_week:
        # Highlight the current week with **week**
        markdown_content += f"| **{week}** | XYZ | @I584002 |\n"
    else:
        # For other weeks, you can specify on-call name and contact details
        markdown_content += f"| {week} | Oncall name | Contact details |\n"

# Write the content to the Markdown file
with open("table.md", "w") as f:
    f.write(markdown_content)
