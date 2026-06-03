#!/bin/bash

podman run --rm -it \
	--env-file test.env \
	-v ./app:/workdir/app:Z \
	-v ./test:/workdir/test:Z \
	-v ./pyproject.toml:/workdir/pyproject.toml:Z \
	-v ./data:/data:Z \
	bna
