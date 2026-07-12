#!/bin/bash

mkdir -p /logs/verifier

# Run pytest and output CTRF format report
pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
exit_code=$?

# Harbor harness requires /logs/verifier/reward.txt
if [ $exit_code -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

exit $exit_code
