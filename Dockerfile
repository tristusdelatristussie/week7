FROM python:3.10

ENV PYTHONUNBUFFERED=TRUE

# -- Install Pipenv:
RUN pip --no-cache-dir install pipenv

# -- Install Application into container:
#RUN set -ex && mkdir /app
#WORKDIR /app

# COPY Pipfile.lock Pipfile.lock
COPY ["Pipfile", "Pipfile.lock", "./"]

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system

# Copy files from host to the container
COPY ["*.ipynb", "*.py", "*.bin", "*.csv", "./"]

# Port where the App will be Exposed
EXPOSE 9797

# Entry point for the application
CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:9797", "api_flask:app"]
