FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml ./
RUN pip install --no-cache-dir -e .

COPY src/ ./src/

ENV PYTHONPATH=/app/src
ENV HOST=0.0.0.0
ENV PORT=8090

EXPOSE 8090

CMD ["python", "-m", "kdd_governance.main"]
