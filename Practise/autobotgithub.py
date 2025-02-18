import os
import time

# Set your repository path
REPO_PATH = "/path/to/your/local/repository"
COMMIT_MESSAGE = "Auto-commit: changes updated"
GIT_USERNAME = "your-github-username"
GIT_TOKEN = "your-github-token"
REPO_URL = f"https://{GIT_USERNAME}:{GIT_TOKEN}@github.com/your-username/your-repository.git"

def git_push():
    os.system(f"cd {REPO_PATH} && git add .")
    os.system(f'cd {REPO_PATH} && git commit -m "{COMMIT_MESSAGE}"')
    os.system(f"cd {REPO_PATH} && git push {REPO_URL} main")

# Run the script every 5 minutes
while True:
    git_push()
    time.sleep(300)  # Sleep for 5 minutes (300 seconds)
