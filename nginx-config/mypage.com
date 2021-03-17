server {
    listen 80;
    server_name domain.com www.domain.com;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/path/to/mypage/mypage.sock;
    }
}