import itertools, csv

members = ["s" + str(s + 1) for s in range(24)]

for r in range(25):
    with open(f'dimensions/{r}.csv', mode='w') as dimension_file:
        writer = csv.writer(dimension_file)

        writer.writerow(['combo number', 'number of members', 'member(s)'])

        combo_number = 0

        combos = itertools.combinations(members, r)
        for y in combos:
            writer.writerow([combo_number, r] + list(y))
            combo_number += 1
        print(f"finished {r}")
