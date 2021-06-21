from python:3.9

RUN pip install poetry

COPY octane11.py /app/octane11.py
COPY pyproject.toml /app/pyproject.toml

WORKDIR /app
RUN poetry install

ENTRYPOINT ["poetry", "run", "python", "/app/octane11.py"]
