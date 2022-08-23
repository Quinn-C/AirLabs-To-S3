#######################################################################
# Base image
#######################################################################

FROM python:3.10-slim as base

RUN pip install poetry==1.1.14

# Set up and become joan user
RUN useradd -m joan
USER joan
RUN mkdir /home/joan/src
WORKDIR /home/joan/src

# Copy project setup files
COPY --chown=joan:joan pyproject.toml .
COPY --chown=joan:joan poetry.lock .
COPY --chown=joan:joan README.md .

# Copy remaining files
COPY --chown=joan:joan Airlabs_api.py .

#######################################################################
# Test image
#######################################################################

FROM base as test

# Install the project locally for testing purposes
RUN poetry install

COPY --chown=joan:joan mypy.ini .

# Copy test directory - once finished will uncomment it - T2
# COPY --chown=joan:joan test test

# Run tests as an entry point
ENTRYPOINT ["poetry", "run", "tox"]
