#!/bin/bash

podman rmi bna
podman build -t bna -f build/Dockerfile .
