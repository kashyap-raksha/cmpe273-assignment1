import sys
from flask import Flask
from github import Github

app = Flask(__name__)

@app.route("/") #home page
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route('/v1/<filename>')
def display(filename):
    argument = str(sys.argv[1])
    url = argument.split("/")[-2:]
    user_name = url[0]
    repo_name = url[1]
    git = Github()
    repo = git.get_user(user_name).get_repo(repo_name)

    if repo.name == "assignment1-config-example":
        if filename.lower().endswith('.yml'):
            if filename.lower() == "dev-config.yml":
                contents = repo.get_file_contents('dev-config.yml')
                return contents.decoded_content
            elif filename.lower() == "test-config.yml":
                contents = repo.get_file_contents('test-config.yml')
                return contents.decoded_content

        elif filename.lower().endswith('.json'):
            if filename.lower() == "dev-config.json":
                file_contents = repo.get_file_contents('dev-config.json')
                return file_contents.decoded_content

            elif filename.lower() == "test-config.json":
                file_contents = repo.get_file_contents('test-config.json')
                return (file_contents).decoded_content

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
