#!/bin/bash

podman run --rm -d \
	--name testdb \
	--env-file test.env \
	--network bna-test-net \
	postgres:18
