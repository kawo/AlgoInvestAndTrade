# shares can be bought one time only
# shares must be bought in full
# 500euros max
import csv

CSV_FILE = "csv/shares.csv"
MAX_COST = 500

shares: list = []

with open(CSV_FILE, newline="") as csvfile:
    shares_file = csv.DictReader(csvfile)
    for row in shares_file:
        shares.append(row)

print(shares)
