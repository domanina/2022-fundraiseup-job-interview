# fundraiseup_job_interview_task
---
Pytest+python+playwright
---
Before running (locally)
---
`pip3 install -r requirements.txt`

`playwright install`

`playwright install-deps`

---
Run tests default (chromium, desktop, headless false)
---
`pytest -v`
---

---
Run tests with diferent browser/device/headless
---

`pytest -v --browser-choice firefox/cromium/webkit --device desktop/iphone --headless` 

Run tests parallel
---
`pytest -n number_of_workers`

Allure
---

run with Allure reports:

`pytest -v --alluredir=allure-results`

start Allure:

`allure serve allure-results`