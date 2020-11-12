FROM alpine:latest

RUN apk update && apk add --no-cache ansible && apk add --no-cache bash && rm -rf /var/cache/apk/*.tar.gz

COPY /assets /opt/resource

CMD [ "ansible-playbook", "--version" ]
