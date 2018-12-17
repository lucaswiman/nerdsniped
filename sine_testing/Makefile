PHONY: test
test: .venv
	USE_REFERENCE_IMPLEMENTATION=1 .venv/bin/pytest test.py
	.venv/bin/pytest test.py

.venv: requirements.txt
	(test -d .venv || python3 -m venv .venv)
	.venv/bin/pip install -r requirements.txt
	touch .venv

