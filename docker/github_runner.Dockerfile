FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y curl git jq sudo build-essential libssl-dev libicu-dev && \
    apt-get clean

RUN useradd -m runner && echo "runner ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

WORKDIR /home/runner


RUN curl -o actions-runner-linux-x64-2.323.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.323.0/actions-runner-linux-x64-2.323.0.tar.gz && \
    tar xzf ./actions-runner-linux-x64-2.323.0.tar.gz && \
    rm actions-runner-linux-x64-2.323.0.tar.gz && \
    ./bin/installdependencies.sh

USER runner
COPY github_runner/entrypoint.sh .

ENTRYPOINT ["./entrypoint.sh"]
