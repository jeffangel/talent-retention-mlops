# First layer
FROM python:3.10-slim AS base
RUN apt-get update && apt-get install -y git curl build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY trainer/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Second layer
FROM python:3.10-slim

RUN apt-get update && apt-get install -y git curl build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=base /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=base /usr/local/bin /usr/local/bin
COPY --from=base /usr/local/include /usr/local/include
    
WORKDIR /app
COPY trainer /app
CMD ["python", "/app/pipelines/dissertation/pipeline.py"]