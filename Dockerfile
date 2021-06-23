FROM python:3.9

RUN pip install poetry

COPY pyproject.toml /app/pyproject.toml

WORKDIR /app
RUN poetry install

COPY octane11.py /app/octane11.py

ENTRYPOINT ["poetry", "run", "python", "/app/octane11.py"]
