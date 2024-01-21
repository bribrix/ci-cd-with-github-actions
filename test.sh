#!/bin/bash

# Define the GitHub repository address
REPO_URL="https://github.com/bribrix/ci-cd-with-github-actions.git"

# Define the directory to clone the repository
CLONE_DIR="my_repo_temp"

# Create a temporary folder to store the repository
mkdir -p $CLONE_DIR

# Clone the repository
git clone $REPO_URL $CLONE_DIR

# Change to the repository directory
cd $CLONE_DIR

# create a virtual environment
python -m venv myenv

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run tests (assuming there's a script or command to run tests)
# Replace 'run-tests-command' with the actual command to run tests

# run the test

python test-app.py

# deactivate the virtual environment
deactivate

# Cleaning up: delete the tmp folder
cd ..
rm -rf $CLONE_DIR

# Exiting the script
exit 0