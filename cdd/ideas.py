# ssh user@server
# wget https://github.com/username/repo/archive/master.zip
# unzip master.zip
# cd repo-master
# python main.py
import cdd
d = cdd.DeployScript()
d.postgresql(migrations="migrations.sql")
d.caddy()
d.install_requirements()
d.create_service()

import some_web_framework
router = some_web_framework.app()
router.get("/", lambda _: "Hello, World!")

if __name__ == "__main__":
    d.run()
    router.run(workers=4, host="0.0.0.0", port=8080)