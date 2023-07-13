import subprocess


def git_clone(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        output = result.stdout
        print("Komut çıktısı:\n", output)
    else:
        error = result.stderr
        print("Hata mesajı:\n", error)
