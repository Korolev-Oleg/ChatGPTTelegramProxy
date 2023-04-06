ssh-keygen -A
sshd -D &
poetry install --no-interaction --no-ansi
python bot.py
wait
