#!/bin/bash

# Define the GitHub repository address
REPO_URL="https://github.com/bribrix/ci-cd-with-github-actions.git"

# Define the directory to clone the repository
CLONE_DIR="my_repo_deployment"

export FLASK_APP=app.py
export FLASK_ENV=development

# Create a temporary folder to store the repository
mkdir -p $CLONE_DIR

# Clone the repository
git clone $REPO_URL $CLONE_DIR

# Change to the repository directory
cd $CLONE_DIR

# Install requirements
pip install -r requirements.txt

# Run the application
nohup flask run &

echo "Python executable: $(which python)"





# Exiting the script
exit 0
