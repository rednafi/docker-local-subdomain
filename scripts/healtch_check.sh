#!/bin/bash

set -euo pipefail

# Run the Python server in the background.
export PORT=5000
nohup node app/app.js >> /dev/null &

# Give the server enough time to be ready before accepting requests.
sleep 2

# Run the health check.
if [[ $(curl -I http://localhost:5000 2>&1) =~ "200 OK" ]]; then
    echo "Health check passed!"
else
    echo "Health check failed!"
    exit 1
fi

# Cleanup.
pkill -9 -ecfi app.js
