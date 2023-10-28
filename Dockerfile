FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python financial_calculators.py