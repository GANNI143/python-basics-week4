from finance_tracker.reports import category_report

def test_category_report():
    data = [{"amount": 100, "category": "Food"}]
    report = category_report(data)
    assert report["Food"] == 100
