import datetime

current_week = datetime.date.today().isocalendar()[1]

markdown_content = f"""\
| Week | Name | Contact details|
|----| ----| ----------|
"""
for week in range(1, 53):
    if week == current_week:
        markdown_content += f"|**{week}** | XYZ | @I584002 |\n"
    else:
        markdown_content += f"| {week} | Oncall name | Contact details| \n"

        with open("table.md" "w") as f:
            f.write(markdown_content)
