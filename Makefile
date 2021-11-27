VENV = flaskenv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

install:
	sudo apt install python3 python3-venv python3-pip
	mkdir VenusFlytrap
	cd VenusFlytrap
	python3 -m venv $(VENV)
	PYTHONPATH=$(VENV) ; . $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

run:
	export FLASK_ENV=development
	$(PYTHON) -m flask run

clean:
	rm -r $(VENV)
	rm -r VenusFlytrap
