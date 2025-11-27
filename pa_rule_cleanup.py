import csv

def generate_sample_report():
    rows = [
        ["Rule Name", "Source", "Destination", "Application", "Action", "Hit Count"],
        ["Allow-Internet", "Any", "Any", "web-browsing", "allow", "1245"],
        ["Test-Rule", "Any", "Any", "any", "deny", "0"]
    ]
    with open("sample_output.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("sample_output.csv created")

if __name__ == "__main__":
    generate_sample_report()