import subprocess
import os

os.environ["PATH"] += os.pathsep + "/path/to/git/bin"


def git_clone(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()  # İşlem tamamlanana kadar bekler

    if process.returncode == 0:
        print("Git klonlama başarılı.")
    else:
        print("Git klonlama hatası:", stderr.decode().strip())


# Örnek repository adresi
repository_url = "https://github.com/openai/gpt-3.5-turkish"

# Git klonlama işlemini çağır
git_clone("git clone http://lore.kernel.org/ath12k/0 ath12k/git/0.git")
print("İşlem bitti")


""" # terminal komutuna erişim
import subprocess

command = "pwd"
result = subprocess.run(command, shell=True, capture_output=True, text=True)

if result.returncode == 0:
    output = result.stdout
    print("Komut çıktısı:\n", output)
else:
    error = result.stderr
    print("Hata mesajı:\n", error)
"""
