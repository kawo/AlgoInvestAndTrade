# shares can be bought one time only
# shares must be bought in full
# 500euros max
import csv
import itertools
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


def append_profit_value(shares: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Calculate and append profit value for each share

    Args:
        shares (List[Dict[str, Any]]): a list of dict with shares

    Returns:
        List[Dict[str, Any]]: the initial list with profit value in it
    """
    for share in shares:
        share["profit"] = share["profit"].replace("%", "").replace(" ", "")
        share["profit"] = int(share["profit"])
        share["cost_per_share"] = int(share["cost_per_share"])
        share["profit_value"] = (share["cost_per_share"] * share["profit"]) / 100
    return shares


def find_best_comb(combs, budget, final: bool = False):
    best_comb = ["temp"]
    best_profit = 0
    final = final
    if final:
        combs_len = len(combs)
        print(combs_len)
        for i in range(0, combs_len):
            for comb in combs:
                comb_len = len(comb)
                print(comb_len)
                for j in range(0, comb_len):
                    print(comb[i][j])
    else:
        for comb in combs:
            comb_len = len(comb)
            cost = 0
            profit = 0
            for i in range(0, comb_len):
                cost += comb[i]["cost_per_share"]
                profit += comb[i]["profit_value"]
            if cost <= budget:
                if profit > best_profit:
                    best_profit = profit
                    best_comb[0] = comb
    if best_comb[0] != "temp":
        return best_comb


def shares_combinations(shares, budget):
    shares_len = len(shares)
    best_combs = []
    best_comb = []
    for i in range(1, (shares_len + 1)):
        combs = itertools.combinations(shares, i)
        best_combs.append(find_best_comb(combs, budget))
    best_combs = list(filter(None, best_combs))
    best_comb = find_best_comb(best_combs, budget, True)
    return best_comb


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
    shares = append_profit_value(shares_dict)
    results = shares_combinations(shares, MAX_COST)
    print(results)
    """results_len = len(results[0])
    print("\nBest combination is:\n")
    cost = 0
    profit = 0
    for i in range(0, results_len):
        cost += results[0][i]["cost_per_share"]
        profit += results[0][i]["profit_value"]
        print(f"{results[0][i]['shares']}")
    print(f"\nTotal cost: {cost}\n")
    print(f"Total profit: {profit}\n")"""
