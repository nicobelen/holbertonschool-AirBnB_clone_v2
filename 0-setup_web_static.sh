#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt update
sudo apt -y install nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html | echo "<html>\n<head>\n</head>\n<body>\nHolberton School\n</body>\n</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu /data/
sed -i "/server;/a \\t location /static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-enabled/default
sudo service nginx restart