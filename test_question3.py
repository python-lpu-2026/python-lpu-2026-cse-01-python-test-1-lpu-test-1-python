import json
from question3 import high_earners_by_department

def test_q3_load_json(tmp_path):          # 4 marks
    f = tmp_path / "e.json"
    f.write_text(json.dumps([
        {"name":"A","department":"IT","salary":60000}
    ]))
    assert high_earners_by_department(str(f), "IT", 50000) == ["A"]

def test_q3_department_filter(tmp_path):  # 4 marks
    f = tmp_path / "e.json"
    f.write_text(json.dumps([
        {"name":"A","department":"HR","salary":60000}
    ]))
    assert high_earners_by_department(str(f), "IT", 50000) == []

def test_q3_salary_filter(tmp_path):      # 4 marks
    f = tmp_path / "e.json"
    f.write_text(json.dumps([
        {"name":"A","department":"IT","salary":40000}
    ]))
    assert high_earners_by_department(str(f), "IT", 50000) == []

def test_q3_sorting(tmp_path):             # 4 marks
    f = tmp_path / "e.json"
    f.write_text(json.dumps([
        {"name":"A","department":"IT","salary":60000},
        {"name":"B","department":"IT","salary":80000}
    ]))
    assert high_earners_by_department(str(f), "IT", 50000) == ["B", "A"]

def test_q3_exception():                   # 4 marks
    assert high_earners_by_department("bad.json", "IT", 50000) == []
