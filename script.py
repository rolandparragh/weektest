import datetime

# Calculate the current week
current_week = datetime.date.today().isocalendar()[1]

# Initialize the HTML content
html_content = f"""\
<table>
  <tr>
    <th>Week</th>
    <th>Name</th>
    <th>Contact details</th>
  </tr>
"""

# Loop through the weeks (1 to 52)
for week in range(1, 53):
    if week == current_week:
        # Highlight the entire row with a yellow background
        html_content += f"""\
  <tr style="background-color: yellow;">
    <td><strong>{week}</strong></td>
    <td><strong>XYZ</strong></td>
    <td><strong>@I584002</strong></td>
  </tr>
"""
    else:
        # For other weeks, specify on-call name and contact details
        html_content += f"""\
  <tr>
    <td>{week}</td>
    <td>Oncall name</td>
    <td>Contact details</td>
  </tr>
"""

html_content += "</table>"

# Write the content to the Markdown file
with open("table.md", "w") as f:
    f.write(html_content)
