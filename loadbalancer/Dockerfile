FROM nginx

RUN apt-get update && apt-get install -y python3 python3-pip curl

RUN curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh

COPY nginx.conf /etc/nginx/nginx.conf
COPY .htpasswd /etc/nginx/.htpasswd
COPY index.html /usr/share/nginx/html/index.html
COPY sd.sh /usr/share/nginx/html/sd.sh
COPY shutdown_server.py /usr/share/nginx/html/shutdown_server.py

RUN chmod +x /usr/share/nginx/html/sd.sh

CMD ["sh", "-c", "python3 /usr/share/nginx/html/shutdown_server.py & nginx -g 'daemon off;'"]