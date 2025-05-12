FROM catthehacker/ubuntu:act-latest

RUN apt-get update && apt-get install -y \
    curl \
    git \
    jq \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install boto3 bentoml

CMD ["tail", "-f", "/dev/null"]
