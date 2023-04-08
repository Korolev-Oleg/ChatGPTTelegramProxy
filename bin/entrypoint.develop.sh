# setup ssh for transfer poetry packages into pycharm
ssh-keygen -A
sshd -D &

# install dependencies
poetry install --no-interaction --no-ansi

# migrate database
python -c "
from db.models import create_all
migrate_all()
"

# start telegram bot
python server.py
