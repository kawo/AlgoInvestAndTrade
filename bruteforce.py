# shares can be bought one time only
# shares must be bought in full
# 500euros max
import csv
import itertools
import math
import timeit
from typing import Any, Dict, List, Tuple

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


def shares_to_centimes(shares: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Convert costs to centimes and append profit value

    Args:
        shares (List[Dict[str, Any]]): a list of dict with shares

    Returns:
        List[Dict[str, Any]]: a list of dict converted to int in centimes
    """
    for share in shares:
        share["profit"] = share["profit"].replace("%", "").replace(" ", "")
        share["profit"] = int(share["profit"])
        share["cost_per_share"] = int(share["cost_per_share"])
        share["profit_value"] = math.ceil(
            (share["cost_per_share"] * share["profit"]) / 100
        )
        print(share)
    return shares


def shares_combinations(shares: List[int], budget: int) -> List[Tuple[int, ...]]:
    combs_list: List[Tuple[int, ...]] = []
    combs_length = len(shares)
    for i in range(1, (combs_length + 1)):
        comb: List[Tuple[int, ...]] = [
            c for c in itertools.combinations(shares, i) if sum(c) <= budget
        ]
        combs_list.append(comb)
    combs_unique: List[Tuple[int, ...]] = []
    result: List[Tuple[int, ...]] = [
        x for x in combs_list if x not in combs_unique and not combs_unique.append(x)
    ]
    result = list(filter(None, result))
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

    # comb_time()

    shares_dict = csv_to_dict(CSV_FILE)
    shares = shares_to_centimes(shares_dict)
    # results = shares_combinations(shares_cost, MAX_COST)

    print(shares)
