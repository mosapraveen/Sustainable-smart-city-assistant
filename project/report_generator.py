def generate_report(data):
    summary = f"Sustainability Report Summary:\n\n{data}"
    with open("sustainability_report.txt", "w") as f:
        f.write(summary)
    return "sustainability_report.txt"
