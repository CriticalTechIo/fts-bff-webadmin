FROM python:3.8-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc libffi-dev g++
WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.2.1

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN . /venv/bin/activate && poetry install --no-dev --no-root

COPY . .
RUN . /venv/bin/activate && poetry build

FROM base as final

WORKDIR /app

RUN groupadd -g 1500 ftsbff && \
    useradd -m -u 1500 -g ftsbff ftsbff

USER ftsbff

COPY --chown=ftsbff:ftsbff --from=builder /venv /venv
COPY --chown=ftsbff:ftsbff --from=builder /app/dist .
COPY --chown=ftsbff:ftsbff docker-entrypoint.sh ./
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ./docker-entrypoint.sh $0 $@
CMD [ "uvicorn", "service.main:app", "--host", "0.0.0.0"]

#RUN . /venv/bin/activate && pip install *.whl
#CMD ["./docker-entrypoint.sh"]