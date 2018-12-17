PHONY: test
test: .venv
	.venv/bin/pytest test.py

.venv: requirements.txt
	(test -d .venv || python3 -m venv .venv)
	.venv/bin/pip install -r requirements.txt

