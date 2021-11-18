VENV = flaskenv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

install:
	sudo apt install python3.8 python3-venv pip
	mkdir VenusFlytrap
	cd VenusFlytrap
	python3 -m venv $(VENV)
	PYTHONPATH=$(VENV) ; . $(VENV)/bin/activate
	$(PIP) install Flask

run:
	export FLASK_APP=main
	$(PYTHON) -m flask run
	
clean:
	rm -r $(VENV)
	rm -r VenusFlytrap
	