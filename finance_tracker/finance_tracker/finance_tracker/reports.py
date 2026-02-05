def category_report(expenses):
    report = {}
    for exp in expenses:
        category = exp["category"]
        report[category] = report.get(category, 0) + exp["amount"]
    return report
