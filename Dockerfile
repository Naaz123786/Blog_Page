# Stage 1: Builder
FROM python:3-alpine AS builder

WORKDIR /app

RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# Stage 2: Runner
FROM python:3-alpine AS runner

WORKDIR /app

COPY --from=builder /app/venv venv
COPY BLOG_PAGE BLOG_PAGE  

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000

EXPOSE ${PORT}

CMD ["python3", "BLOG_PAGE/manage.py", "runserver", "0.0.0.0:8000"]
