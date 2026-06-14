import csv, random

mountains = {"Everest": "Nepal", "Elbrus": "Russia", "Mont Blanc": "France", "Kilimanjaro": "Tanzania", "Denali": "USA"}

d = ["easy", "medium", "hard"]

with open("/app/data/data.csv", "w", newline="") as f:
    w = csv.writer(f)

    w.writerow(["id", "mountain", "country", "height", "difficulty"])

    names = list(mountains.keys())

    for i in range(10):
        mountain = random.choice(names)

        w.writerow([i + 1, mountain, mountains[mountain], random.randint(1000, 9000), random.choice(d)])

print("mountain csv created")