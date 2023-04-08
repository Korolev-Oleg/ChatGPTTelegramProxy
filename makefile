migrate:
	docker exec -it gpt-proxy-bot python3 -c "from db.models import create_all; create_all()"

ipython:
	docker exec -it gpt-proxy-bot ipython

kill:
	docker kill gpt-proxy-bot

recreate:
	make kill
	make remove
	make create
	make start

remove:
	docker rm gpt-proxy-bot

enable_ssh:
	docker exec -it gpt-proxy-bot ./bin/enable-ssh.sh

create:
	docker run --name=gpt-proxy-bot -d -p 2222:22 -v `pwd`:/opt/app gpt-proxy

start:
	docker start gpt-proxy-bot
	make enable_ssh

build:
	docker build -t gpt-proxy .

restart:
	make kill
	make start


normalize_access:
	docker exec -it gpt-proxy-bot chmod -R 777 ./

shell:
	docker exec -it gpt-proxy-bot zsh
