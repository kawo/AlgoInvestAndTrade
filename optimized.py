import csv
import timeit
from typing import Any, Dict, List

BUDGET = 500
SHARES_FILE = "csv/shares.csv"
DATASET1 = "csv/dataset1_Python+P7.csv"
DATASET2 = "csv/dataset2_Python+P7.csv"


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
        share["profit_value"] = share["cost_per_share"] * share["profit"]
    return shares


"""Implementing the knapsack algorithm:

    columns == budget (weight)
    rows == shares (goods with price)
"""


def knapsack(budget: int, share_cost, share_value):
    """Knapsack algorithm implementation to find the best profit

    Args:
        budget (int): the max budget (columns for the knapsack)
        share_cost (list[int]): share cost (rows for the knapsack)
        share_value (list[int]): share profit value (values for the knapsack)

    Returns:
        bag: last cell with the best profit
    """
    n = len(share_value)
    bag = [[0 for x in range(budget + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for j in range(budget + 1):
            if i == 0 or j == 0:
                bag[i][j] = 0
            elif share_cost[i - 1] <= j:
                bag[i][j] = max(
                    share_value[i - 1] + bag[i - 1][j - share_cost[i - 1]],
                    bag[i - 1][j],
                )
            else:
                bag[i][j] = bag[i - 1][j]
    return bag[n][budget] / 100


def knapsack_time():
    SETUP_CODE = """
from __main__ import csv_to_dict
from __main__ import append_profit_value
from __main__ import knapsack
import csv
from typing import Any, Dict, List
SHARES_FILE = "csv/shares.csv"
shares = append_profit_value(csv_to_dict(SHARES_FILE))
share_cost = []
share_value = []
for share in shares:
    share_cost.append(share["cost_per_share"])
    share_value.append(share["profit_value"])
budget = 500"""
    TEST_CODE = """
knapsack(budget, share_cost, share_value)"""

    times = timeit.timeit(stmt=TEST_CODE, setup=SETUP_CODE, number=1)

    return print(f"\nKnapsack calc time: {times}s")


if __name__ == "__main__":

    # knapsack_time()

    """shares = append_profit_value(csv_to_dict(SHARES_FILE))

    share_cost = []
    share_value = []
    for share in shares:
        share_cost.append(share["cost_per_share"])
        share_value.append(share["profit_value"])

    print(f"\n{knapsack(BUDGET, share_cost, share_value)}\n")"""

    dataset1 = csv_to_dict(DATASET1)
    dataset1_cost = []
    dataset1_value = []
    for data in dataset1:
        if (float(data["price"]) > 0) and (float(data["profit"]) > 0):
            dataset1_cost.append(int(float(data["price"]) * 100))
            dataset1_value.append(int(float(data["profit"]) * 100))

    dataset2 = csv_to_dict(DATASET2)
    dataset2_cost = []
    dataset2_value = []
    for data in dataset2:
        if (float(data["price"]) > 0) and (float(data["profit"]) > 0):
            dataset2_cost.append(int(float(data["price"]) * 100))
            dataset2_value.append(int(float(data["profit"]) * 100))

    print(f"\n{knapsack(BUDGET * 100, dataset1_cost, dataset1_value)}\n")

    print(f"\n{knapsack(BUDGET * 100, dataset2_cost, dataset2_value)}\n")
