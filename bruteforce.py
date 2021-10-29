# shares can be bought one time only
# shares must be bought in full
# 500euros max
import csv
from typing import Dict, List

CSV_FILE = "csv/shares.csv"
MAX_COST = 500


def csv_to_dict(file: str) -> List[Dict[str, str]]:
    """Read CSV file and convert it to list of Dict

    Args:
        file (str): const var with file url

    Returns:
        List[Dict[str, str]]: a list of Dict from CSV file
    """
    shares: List[Dict[str, str]] = []

    with open(file, newline="") as csvfile:
        shares_file = csv.DictReader(csvfile)
        for row in shares_file:
            shares.append(row)
    return shares


def extract_shares_cost(shares: List[Dict[str, str]]) -> List[int]:
    """Extract each share cost and create a List

    Args:
        shares (List[Dict[str, str]]): list of Dict from csv_to_dic func

    Returns:
        List[int]: list of share cost
    """
    shares_cost: List[int] = []
    for share in shares:
        shares_cost.append(int(share["cost_per_share"]))
    return shares_cost


shares_dict = csv_to_dict(CSV_FILE)

print(extract_shares_cost(shares_dict))
