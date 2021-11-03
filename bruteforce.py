# shares can be bought one time only
# shares must be bought in full
# 500euros max
import csv
import itertools
import timeit
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


def shares_combinations(shares: List[int], budget: int):
    combs_list = []
    combs_length = len(shares)
    for i in range(1, (combs_length + 1)):
        comb = [c for c in itertools.combinations(shares, i) if sum(c) <= budget]
        combs_list.append(comb)
    combs_unique = []
    result = [
        x for x in combs_list if x not in combs_unique and not combs_unique.append(x)
    ]
    print("Length of original comb:", len(combs_list))
    print("Length w/o duplicates:", len(result))
    return result


def comb_time():
    SETUP_CODE = """
from __main__ import csv_to_dict
from __main__ import extract_shares_cost
from __main__ import shares_combinations
import csv
import itertools
from typing import Dict, List
CSV_FILE = "csv/shares.csv"
MAX_COST = 500
shares_dict = csv_to_dict(CSV_FILE)
shares_cost = extract_shares_cost(shares_dict)"""
    TEST_CODE = """
shares_combinations(shares_cost, MAX_COST)"""

    times = timeit.timeit(stmt=TEST_CODE, setup=SETUP_CODE, number=1)

    return print("Combs calc time:", times)


if __name__ == "__main__":
    comb_time()
