# shares can be bought one time only
# shares must be bought in full
# 500euros max
import csv
from typing import Dict, List, Tuple

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


def extract_shares_cost(shares: List[Dict[str, str]]) -> Dict[str, int]:
    """Extrat each share cost and register them in Dict

    Args:
        shares (List[Dict[str, str]]): list of dict generated from csv_to_dict func

    Returns:
        Dict[str, int]: Dict with Action-#: cost
    """
    shares_cost: List[Tuple[str, int]] = []
    for share in shares:
        share_cost = (share["shares"], int(share["cost_per_share"]))
        shares_cost.append(share_cost)
    return dict(shares_cost)


shares_dict = csv_to_dict(CSV_FILE)

print(extract_shares_cost(shares_dict))
