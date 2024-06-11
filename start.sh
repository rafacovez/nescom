#!/bin/bash

if [ "$1" == "development" ]; then
  echo "Starting development environment"
  (cd server && npm run start:dev) &
  server_pid=$!
  (cd client && npm run serve)
  client_pid=$!
elif [ "$1" == "production" ]; then
  echo "Starting production environment"
  (cd client && npm run build) &
  client_pid=$!
  wait
  (cd server && npm run start:prod)
  server_pid=$!
else
  echo "Please specify the environment (development or production)"
fi

trap "kill $server_pid $client_pid; exit" SIGINT

wait
