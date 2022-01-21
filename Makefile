VENV = flaskenv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
ACTIVATE = . /app/$(VENV)/bin/activate

install:
	mkdir VenusFlytrap
	cd VenusFlytrap
	python3 -m venv $(VENV)
	PYTHONPATH=$(VENV); . $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

run:
	$(ACTIVATE) && flask run --debugger

test:
	$(PYTHON) -m pytest -vvv

clean:
	rm -r $(VENV)
	rm -r VenusFlytrap