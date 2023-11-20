import subprocess


def setupEnv()-> None:
    subprocess.run(["python", "-m", "ensurepip", "--upgrade"])
    subprocess.run(["pip", "install", "pipreqs"])
    subprocess.run(["pipreqs", ".", "--force"])
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    subprocess.run(["clear"])


def setupAccess() -> None:
    token = input("Please provide API access token: ")
    with open(".accesstoken", "w") as f:
        f.write(token)


if __name__ == '__main__':
    setupEnv()
    setupAccess()