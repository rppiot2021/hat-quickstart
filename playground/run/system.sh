#!/bin/bash

export PYTHONPATH=../../src_py
python -m hat.orchestrator.main --conf ./data/orchestrator.yaml
