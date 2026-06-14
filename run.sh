#!/bin/bash

if [ "$1" = "build_generator" ]; then
    docker build -t generator-image ./generator
fi

if [ "$1" = "run_generator" ]; then
    docker run --rm -v "$(pwd)/data:/app/data" generator-image
fi

if [ "$1" = "clear_data" ]; then
    rm -f data/*
fi

if [ "$1" = "structure" ]; then
    ls -R
fi