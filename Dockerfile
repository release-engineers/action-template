FROM alpine:3.18.0 as staging

RUN apk add --no-cache unzip

ADD .venv/lib/python3.11/site-packages /app
ADD dist/*.whl /tmp/dist/
RUN unzip -n -q /tmp/dist/*.whl -d /app

FROM python:3.11-alpine

LABEL org.opencontainers.image.source=https://github.com/release-engineers/action-template

ENV PYTHONPATH=/app:$PYTHONPATH
COPY --from=staging /app/ /app/

ENTRYPOINT ["python", "-m", "action_template"]
