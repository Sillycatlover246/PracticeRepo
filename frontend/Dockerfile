FROM nginx:1.27.0
#cd frontend -> docker build -t mysite .
RUN rm -rf /usr/share/nginx/html
COPY static /usr/share/nginx/html
#docker run -p 80:80 mysite