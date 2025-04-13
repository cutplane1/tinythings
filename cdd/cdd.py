import subprocess
import os
import sys
import platform

def check_call(cmd):
    try:
        _ = subprocess.check_call(cmd)
        return True
    except subprocess.CalledProcessError:
        return False

class Platform:
    def __init__(self):
        self.kernel = os.name
        self.distro = self.detect_distro()
        self.init = self.detect_init()
    
    def detect_distro(self):
        if self.kernel == "nt":
            return platform.release()
        elif self.kernel == "posix":
            if check_call("apt -h"):
                return "Debian"
            elif check_call("dnf -h"):
                return "Fedora"
        else:
            return "Generic"
    
    def detect_init(self):
        if self.kernel == "nt":
           return "windows-init"
        elif self.kernel == "posix":
            if check_call("systemctl -h"):
                return "systemd"
            else:
                return "TODO"
    
class DeployScript:
    def __init__(self):
        self.platform = Platform()

    def postgresql(self, migrations):
        # if self.platform.distro == "Debian":
            # subprocess.check_call(["sudo apt install -y postgresql"])
        # other distros
        # start service
        # run migrations
        pass

    def caddy(self):
        pass

    def create_service(self):
        # create and start service (with dependencies)
        pass

    def install_requirements(self):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])