clean:
	find . | grep __pycache__ | xargs rm -rf

fmt:
	black src --safe

lint:
	pylava -o pylava.ini src tests

test:
	tox
