import re

# File paths
index_file = "index_base.html"
app_file = "app.py"
output_file = "index.html"

# Read the current index.html
with open(index_file, "r", encoding="utf-8") as f:
    index_html = f.read()

# Read the content of app.py
with open(app_file, "r", encoding="utf-8") as f:
    app_content = f.read()

# Escape backslashes and backticks for use in a JS template string
app_content_escaped = app_content.replace("\\", "\\\\").replace("`", "\\`")

# Replace the multiline string assigned to "Introduction.py"
new_index_html = re.sub(
    r'"app\.py": `.*?`',
    f'"app.py": `{app_content_escaped}`',
    index_html,
    flags=re.DOTALL
)

# Write the result
with open(output_file, "w", encoding="utf-8") as f:
    f.write(new_index_html)

print(f"Updated HTML written to {output_file}")
