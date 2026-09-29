# Chapter 3 Assessment — Seed inventory

This is a **timed, graded assessment**. You have **33 minutes**. You may attempt the tiers in any order.

Write your code in `src/seed_inventory.py`. The data is already there.

## Checking your work

**There are no tests.** The expected outputs below are how you check your work. Run the file and compare what it prints with this README:

```
python src/seed_inventory.py
```

## Grade bands

| Completed                     | Grade |
|-------------------------------|-------|
| 1 of the two Tier B functions | C+    |
| both Tier B functions         | B     |
| + `stock_flags`               | B+    |
| + `low_stock`                 | A-    |
| + `grower_count`              | A     |
| + `seed_report`               | A+    |

## Data

```python
seeds = [
    {"name": "  Sugar Snap Pea (50g) ", "grower": "FIELDSTONE FARMS",   "in_stock": 30,  "reorder_at": 45},
    {"name": "Marigold Mix (packet)",   "grower": "verdant seed co",    "in_stock": 210, "reorder_at": 120},
    {"name": " Heirloom Tomato (25g) ", "grower": "Fieldstone Farms",   "in_stock": 88,  "reorder_at": 88},
    {"name": "Basil Genovese (10g)",    "grower": "VERDANT SEED CO",    "in_stock": 16,  "reorder_at": 40},
    {"name": "  Pumpkin Howden",        "grower": "orchard lane seeds", "in_stock": 140, "reorder_at": 60},
]
```

- "Below the reorder point" means strictly below. A seed sitting exactly at its reorder point is OK.
- A seed with no parenthetical in its name is still a valid name.

---

## Tier B: chained string methods, map, a lambda

**Constraint:** Each body is a single `return` statement. No loops and no list comprehensions.

### 1. `clean_name(name: str) -> str`

The name with the parenthetical size removed and the whitespace trimmed.

```python
clean_name("  Sugar Snap Pea (50g) ")   # 'Sugar Snap Pea'
clean_name(" Heirloom Tomato (25g) ")   # 'Heirloom Tomato'
clean_name("  Pumpkin Howden")          # 'Pumpkin Howden'
```

### 2. `grower_codes(seeds: list) -> list`

Each grower as a lowercase code with spaces replaced by underscores. You must use `map()` and a lambda.

```python
grower_codes(seeds)
['fieldstone_farms', 'verdant_seed_co', 'fieldstone_farms', 'verdant_seed_co', 'orchard_lane_seeds']
```

---

## Tier B+: a conditional expression inside the lambda

**Constraint:** You must use `map()` and a lambda. The body is a single `return` statement. No loops and no list comprehensions.

### 3. `stock_flags(seeds: list) -> list`

For each seed, the string `"Reorder"` if its stock has fallen **below** its reorder point, `"OK"` otherwise. A plain list of strings.

```python
stock_flags(seeds)
['Reorder', 'OK', 'OK', 'Reorder', 'OK']
```

---

## Tier A-: filter and map combined

**Constraint from here on:** No loops. Bodies may be more than one line, and you choose the structure. You must use both `map()` and `filter()`.

### 4. `low_stock(seeds: list) -> list`

For every seed that has fallen below its reorder point, a dict with `"name"` (cleaned as in function 1) and `"short_by"` (how many units below the reorder point it is).

```python
low_stock(seeds)
[{'name': 'Sugar Snap Pea', 'short_by': 15}, {'name': 'Basil Genovese', 'short_by': 24}]
```

---

## Tier A: filter and a combine step

### 5. `grower_count(seeds: list, grower: str) -> int`

How many seed varieties come from the given grower. The grower arrives as a code in the same form function 2 produces.

```python
grower_count(seeds, "fieldstone_farms")     # 2
grower_count(seeds, "verdant_seed_co")      # 2
grower_count(seeds, "orchard_lane_seeds")   # 1
grower_count(seeds, "sunridge_seed")        # 0
```

---

## Tier A+: pull it together

### 6. `seed_report(seeds: list, grower: str) -> dict`

Everything from one grower that needs reordering, as a single dictionary with the keys `"count"` (how many seeds), `"names"` (their cleaned names), and `"units"` (the total number of units short across all of them).

```python
seed_report(seeds, "fieldstone_farms")     # {'count': 1, 'names': ['Sugar Snap Pea'], 'units': 15}
seed_report(seeds, "verdant_seed_co")      # {'count': 1, 'names': ['Basil Genovese'], 'units': 24}
seed_report(seeds, "orchard_lane_seeds")   # {'count': 0, 'names': [], 'units': 0}
seed_report(seeds, "sunridge_seed")        # {'count': 0, 'names': [], 'units': 0}
seed_report([], "fieldstone_farms")        # {'count': 0, 'names': [], 'units': 0}
```
