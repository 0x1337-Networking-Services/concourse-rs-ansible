FROM alpine:latest

RUN apk update && apk add --no-cache ansible && apk add --no-cache bash && apk add --no-cache openssh-client && apk add --no-cache sshpass && rm -rf /var/cache/apk/*.tar.gz

COPY /assets /opt/resource

CMD [ "ansible-playbook", "--version" ]
