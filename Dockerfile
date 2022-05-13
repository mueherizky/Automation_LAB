FROM ubuntu:latest
RUN apt update && \
    apt install dnsutils iputils-ping traceroute nmap net-tools yersinia -y