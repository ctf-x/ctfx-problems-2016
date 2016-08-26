FROM debian:8

RUN apt-get update
RUN apt-get install -y socat
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get install -y build-essential

RUN gcc -o dat_boinary -m32 -fno-stack-protector dat_boinary.c
RUN rm dat_boinary.c
RUN socat tcp-listen:1337,fork,reuseaddr exec:”./dat_boinary"