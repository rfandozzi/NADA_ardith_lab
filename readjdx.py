import csv

input_path = "12125-02-9-IR.jdx"
output_path = "12125-02-9-IR_raw.csv"

# Use latin-1 encoding to avoid UnicodeDecodeError
with open(input_path, "r", encoding="latin-1") as infile:
    lines = infile.readlines()

with open(output_path, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    for line in lines:
        writer.writerow([line.strip()])


