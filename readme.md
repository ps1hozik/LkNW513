1. Установить необходимые пакеты:

   `sudo apt update`

   `sudo apt install -y python3 python3-venv postgresql nginx`

2. Именить права доступа:

   > &lt;username&gt; заменить на своего пользователя

   `sudo usermod -aG www-data <username>`

   `sudo chown -R www-data:www-data /var/www/`

   `sudo chmod -R 770 /var/www/`

3. Склонировать репозиторий в папку /var/www/LkNW513, перейти в созданную директорию:

   `git clone https://github.com/ps1hozik/LkNW513.git /var/www/LkNW513`

   `cd /var/www/LkNW513`

4. Создать и активировать виртуальное окружение:

   `python3 -m venv venv`

   `source venv/bin/activate`

5. Установить необходимые пакеты:

   `pip install -r requirements.txt`

6. Создать базу даных:

   `sudo -i -u postgres`

   `psql`

   `CREATE DATABASE forms_db;`

   > root заменить на любой пароль

   `ALTER USER postgres WITH PASSWORD 'root';`

   > для выхода нажать два раза CTRL+D

7. Переместить файл config/LkNW513.service в /etc/systemd/system:

   > изменить root в 10 строке если меняли ранее

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
