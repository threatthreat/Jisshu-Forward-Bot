#!/bin/bash

echo "Cloning Repo...."
if [ -z "$BRANCH" ]; then
  echo "Cloning main branch...."
  git clone https://github.com/Jisshubot/Jisshu-forward-bot Jisshubot
else
  echo "Cloning $BRANCH branch...."
  git clone -b "$BRANCH" https://github.com/Jisshubot/Jisshu-forward-bot Jisshubot
fi

cd Jisshubot || exit 1

# Install dependencies
pip install --no-cache-dir -r requirements.txt

echo "Starting Flask app on port 8080 for health check..."
gunicorn app:app --bind 0.0.0.0:8080 &

# Give Flask some time to start
sleep 2

echo "Starting Forward Bot..."
python3 main.py
