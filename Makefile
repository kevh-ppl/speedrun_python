SHELL := /bin/bash
IMAGE := speedrun-python:latest
MOD   ?=

.PHONY: help build shell test lint typecheck clean rebuild

help:
	@echo "Targets:"
	@echo "  build       - construye la imagen Docker del lab"
	@echo "  shell       - abre bash dentro del contenedor (monta el proyecto)"
	@echo "  test        - corre pytest sobre todos los modulos (o MOD=NN-nombre)"
	@echo "  lint        - ruff check sobre ejercicios y solucion"
	@echo "  typecheck   - mypy --strict sobre solucion/"
	@echo "  rebuild     - fuerza reconstruccion sin cache"
	@echo "  clean       - borra la imagen"

build:
	docker build -t $(IMAGE) -f docker/Dockerfile .

rebuild:
	docker build --no-cache -t $(IMAGE) -f docker/Dockerfile .

shell: build
	docker run --rm -it \
		--hostname speedrun-py \
		-v $(PWD):/lab \
		-w /lab \
		$(IMAGE) bash

test: build
	docker run --rm \
		-v $(PWD):/lab \
		-w /lab \
		$(IMAGE) bash bin/run-tests.sh $(MOD)

lint: build
	docker run --rm \
		-v $(PWD):/lab \
		-w /lab \
		$(IMAGE) bash -c 'ruff check .'

typecheck: build
	docker run --rm \
		-v $(PWD):/lab \
		-w /lab \
		$(IMAGE) bash -c 'find . -type d -name solucion -not -path "*/\.*" -print0 | xargs -0 -I{} mypy --strict {} || true'

clean:
	-docker rmi $(IMAGE)
