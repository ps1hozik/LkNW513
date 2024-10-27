1. Установить необходимые пакеты:

   `sudo apt update`

   `sudo apt install -y python3 python3-venv postgresql nginx`

2. Склонировать репозиторий в папку /home/&lt;user&gt;/LkNW513, перейти в созданную директорию:

   > &lt;user&gt; заменить на своего пользователя

   `git clone https://github.com/ps1hozik/LkNW513.git /home/<user>/LkNW513`

   `cd /home/<user>/LkNW513`

3. Создать и активировать виртуальное окружение:

   `python3 -m venv venv`

   `source venv/bin/activate`

4. Установить необходимые пакеты:

   `pip install -r requirements.txt`

5. Создать базу даных:

   `sudo -i -u postgres`

   `psql`

   `CREATE DATABASE forms_db;`

   > &lt;password&gt; заменить на любой пароль

   `ALTER USER postgres WITH PASSWORD '<password>';`

6. Изменить права доступа:

   `sudo chown -R www-data:www-data /home/<user>/LkNW513`

   `sudo find /home/<user>/LkNW513 -type d -exec chmod 755 {} \;`

   `sudo find /home/<user>/LkNW513 -type f -exec chmod 644 {} \;`

7. Переместить файл config/LkNW513.service в /etc/systemd/system:

   > изменить &lt;password&gt; в 10 строке на ранее созданный для postgres

   `sudo mv config/LkNW513.service /etc/systemd/system`

8. Запустить Gunicorn:

   `sudo systemctl daemon-reload`

   `sudo systemctl start LkNW513`

   `sudo systemctl enable LkNW513`

   > для проверки статуса использовать `sudo systemctl status LkNW513`

9. Переместить файл config/LkNW513 в /etc/nginx/sites-available/:

   > прежде изменить server_name, для запуска не на localhost

   `sudo mv config/LkNW513 /etc/nginx/sites-available/`

10. Активировать конфигурации Nginx:

    `sudo ln -s /etc/nginx/sites-available/LkNW513 /etc/nginx/sites-enabled`

    > проверить на наличие ошибок `sudo nginx -t`

    `sudo systemctl restart nginx`
