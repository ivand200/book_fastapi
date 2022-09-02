# git init
# git add hello.txt
# git commit -m "Initial commit"
# git status 
# git diff <file>
# touch .gitignore 
# echo ".env" >> .gitignore (*.env, env/venv, .vscode, .idea)

# git checkout -b hello-branch 
# git checkout main


# Virtual env
# mkdir todos && cd todos
# python3 -m venv venv 
# sorce venv/bin/activate
# You can also use poetry, pipenv
# python3 -m pip list -> verify whether pip is installed


# Basic commands
# pip install fastapi
# pip uninstall fastapi
# pip freeze > requirements.txt
# pip install -r requirements.txt


# Docker
# FROM PYTHON:3.8
# Set working directory to /usr/src/app
# WORKDIR /usr/src/app
# Copy the contents of the current local directory into
# the container's working directory
# ADD . /usr/src/app
# Run a command
# CMD ["python", "hello.py"]

# docker build -t getting_started .
# docker build -t api api/Dockerfile
# docker run getting-started


# pip install fastapi uvicorn

# uvicorn api:app --port 8000 --reload
