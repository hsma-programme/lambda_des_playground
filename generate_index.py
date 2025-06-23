import re

# File paths
template_file = "template_index.html"
app_file = "app.py"
output_file = "index.html"

# Read files
with open(template_file, "r", encoding="utf-8") as f:
    template_html = f.read()

with open(app_file, "r", encoding="utf-8") as f:
    app_content = f.read()

# Escape backslashes and backticks for JS template literal
app_content_escaped = app_content.replace("\\", "\\\\").replace("`", "\\`")

# Add leading newline for formatting
replacement_code = f"`\n{app_content_escaped}`"

# Replace the mount(...) argument — matching between the first and last backticks in the call
new_html = re.sub(
    r"mount\(\s*`.*?`\s*,",
    f"mount({replacement_code},",
    template_html,
    flags=re.DOTALL
)

# Write the updated HTML
with open(output_file, "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"Updated HTML written to {output_file}")
