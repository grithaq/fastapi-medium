run-server:
	PYTHONPATH=src uvicorn --reload main:app --host 0.0.0.0 --port 8000


run-test:
ifdef dst
	PYTHONPATH=src python -m pytest $(dst) -v
else
	PYTHONPATH=src python -m pytest -v
endif
