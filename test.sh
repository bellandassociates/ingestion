#!/bin/bash

podman run --rm -it \
	-v ./app:/workdir/app:Z \
	-v ./test:/workdir/test:Z \
	-v ./pytest.ini:/workdir/pytest.ini:Z \
	-v ./data:/data:Z \
	--network bna-test-net \
	--env-file test.env \
	bna bash -c "pytest" \
	| tee artifacts/pytest_output.txt
