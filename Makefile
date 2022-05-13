.PHONY: init
init:
	@npm install


.PHONY: lint
lint:
	@npx eslint
	@npx prettier app/app.ts --write


.PHONY: lint-check
lint-check:
	@npx eslint
	@npx prettier app/app.ts --check


.PHONY: devserver
devserver:
	@node app.js


.PHONY: tsc
tsc:
	@npx tsc


.PHONY: build
build: tsc
	@docker compose up --build


.PHONY: up
up:
	@docker compose up


.PHONY: upd
upd:
	@docker compose up -d


.PHONY: health_check
health-check:
	@chmod +x ./scripts/*
	@./scripts/health_check.sh
