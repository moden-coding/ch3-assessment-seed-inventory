seeds = [
    {"name": "  Sugar Snap Pea (50g) ", "grower": "FIELDSTONE FARMS",   "in_stock": 30,  "reorder_at": 45},
    {"name": "Marigold Mix (packet)",   "grower": "verdant seed co",    "in_stock": 210, "reorder_at": 120},
    {"name": " Heirloom Tomato (25g) ", "grower": "Fieldstone Farms",   "in_stock": 88,  "reorder_at": 88},
    {"name": "Basil Genovese (10g)",    "grower": "VERDANT SEED CO",    "in_stock": 16,  "reorder_at": 40},
    {"name": "  Pumpkin Howden",        "grower": "orchard lane seeds", "in_stock": 140, "reorder_at": 60},
]


# === TIER B ===
# Must use map() and a lambda. Body is a single return statement.
# No loops, no list comprehensions.

def seed_names(seeds: list) -> list:
    """Return each name with the parenthetical size removed and the
    whitespace trimmed."""
    pass


def grower_codes(seeds: list) -> list:
    """Return each grower as a lowercase code with spaces replaced by
    underscores."""
    pass


# === TIER B+ ===
# Same constraint as Tier B.

def stock_flags(seeds: list) -> list:
    """Return "Reorder" for each seed whose stock has fallen below its
    reorder point, "OK" otherwise."""
    pass


# === TIER A-, A and A+ ===
# No loops. Bodies may be more than one line. map() and filter() must both
# be used.

def low_stock(seeds: list) -> list:
    """For every seed below its reorder point, return a dict with keys
    "name" (cleaned as in seed_names) and "short_by" (how many units below
    the reorder point it is)."""
    pass


def grower_count(seeds: list, grower: str) -> int:
    """Return how many seed varieties come from the given grower. The grower
    is a code in the same form grower_codes produces."""
    pass


def seed_report(seeds: list, grower: str) -> dict:
    """Return everything from one grower that needs reordering, as a dict
    with keys "count" (how many seeds), "names" (their cleaned names) and
    "units" (the total number of units short across all of them)."""
    pass


def main():
    print("seed_names:  ", seed_names(seeds))
    print("grower_codes:", grower_codes(seeds))
    print("stock_flags: ", stock_flags(seeds))
    print("low_stock:   ", low_stock(seeds))
    print()
    print('grower_count(seeds, "fieldstone_farms"):  ', grower_count(seeds, "fieldstone_farms"))
    print('grower_count(seeds, "verdant_seed_co"):   ', grower_count(seeds, "verdant_seed_co"))
    print('grower_count(seeds, "orchard_lane_seeds"):', grower_count(seeds, "orchard_lane_seeds"))
    print('grower_count(seeds, "sunridge_seed"):     ', grower_count(seeds, "sunridge_seed"))
    print()
    print('seed_report(seeds, "fieldstone_farms"):  ', seed_report(seeds, "fieldstone_farms"))
    print('seed_report(seeds, "verdant_seed_co"):   ', seed_report(seeds, "verdant_seed_co"))
    print('seed_report(seeds, "orchard_lane_seeds"):', seed_report(seeds, "orchard_lane_seeds"))
    print('seed_report(seeds, "sunridge_seed"):     ', seed_report(seeds, "sunridge_seed"))
    print('seed_report([], "fieldstone_farms"):     ', seed_report([], "fieldstone_farms"))


if __name__ == "__main__":
    main()
