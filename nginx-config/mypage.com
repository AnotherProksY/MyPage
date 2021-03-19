server {
    server_name domain.com;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/path/to/mypage/mypage.sock;
    }   

    location /static/ {
        alias /path/to/mypage/static/;
    }   

    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/doamin.com/fullchain.pem; #    managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem; #  managed by Certbot 
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}

server {
    if ($host = domain.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


    listen 80;
    server_name domain.com;
    return 404; # managed by Certbot

}