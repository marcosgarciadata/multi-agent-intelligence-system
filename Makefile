install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	flake8 src/

docker-build:
	docker build -t multi-agent-intelligence-system .

docker-run:
	docker run -p 8000:8000 multi-agent-intelligence-system
