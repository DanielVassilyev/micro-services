FROM golang:1.23

WORKDIR /app

RUN apt-get update && apt-get install -y procps coreutils

COPY service2/service2.go service2/go.mod /app/

RUN go build -v -o service2

EXPOSE 8500

CMD ["/app/service2"]
