.PHONY: install eval-all eval-classifier eval-classifier-prompt test

install:
	pip install -e ".[dev]"

eval-classifier:
	cd services/ticket-classifier && MOCK_LLM=1 scaffold run

eval-classifier-prompt:
	cd services/ticket-classifier && MOCK_LLM=1 ../../shared/scripts/scaffold_run.sh --config scaffold-prompt.yaml

eval-all:
	$(MAKE) eval-classifier
	$(MAKE) eval-classifier-prompt
	cd services/rag-qa && MOCK_LLM=1 scaffold run
	cd services/json-api && MOCK_LLM=1 scaffold run
	cd services/support-agent && MOCK_LLM=1 ../../shared/scripts/scaffold_run.sh --config scaffold-single.yaml
	cd services/support-agent && MOCK_LLM=1 ../../shared/scripts/scaffold_run.sh --config scaffold-multi.yaml
	cd services/summarizer && MOCK_LLM=1 ../../shared/scripts/scaffold_run.sh --config scaffold-mock.yaml

test:
	pytest shared/ services/ -q
