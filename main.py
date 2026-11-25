import os

# One-line roast of a daily gadget: the laptop trackpad's palm rejection.
ROAST = (
    "Palm rejection on my laptop is flawless: my thumb is invisible while I "
    "type, then it reads my palm the moment I pause, so the cursor lands ten "
    "minutes in the past."
)

# Output lands in /output/entry.txt unless the runner overrides the directory.
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

# Write the roast as a single line, UTF-8, with no trailing newline.
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ROAST)
