import csv

rows = []

with open("/app/data/data.csv") as f:
    r = csv.DictReader(f)

    for row in r:
        rows.append(row)

html = "<html><body><h1>Mountain report</h1><table border='1'>"

html += "<tr><th>ID</th><th>Mountain</th><th>Country</th><th>Height</th><th>Difficulty</th></tr>"

for row in rows:
    html += f"<tr><td>{row['id']}</td><td>{row['mountain']}</td><td>{row['country']}</td><td>{row['height']}</td><td>{row['difficulty']}</td></tr>"

html += "</table></body></html>"

with open("/app/data/report.html", "w") as f:
    f.write(html)

print("html report created")