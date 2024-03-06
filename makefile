run-server:
	PYTHONPATH=app uvicorn --reload main:app --host 0.0.0.0 --port 8000

run-test:
ifdef dst
	PYTHONPATH=app python -m pytest $(dst) -v
else
	PYTHONPATH=app python -m pytest -v
endif
