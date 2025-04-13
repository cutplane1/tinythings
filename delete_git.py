import os
import shutil

current_dir = os.getcwd()

folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))]
folders.remove(".git")
for f in folders:
    try:
        path = os.path.join(current_dir, f, ".git")
        # shutil.rmtree(path) doesnt work (WinError 5)
        if os.path.exists(path):
            if os.name == "nt":
                os.system(f"rd /s /q {path}")
            else:
                os.system(f"rm -rf {path}")

    except Exception as e:
        print(e)



