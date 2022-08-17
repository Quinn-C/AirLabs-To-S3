#######################################################################
# Base image
#######################################################################

FROM python:3.10.6-slim as base

RUN pip install poetry==1.1.14

# Set up and become kip user
RUN useradd -m kip
USER kip
RUN mkdir /home/kip/src
WORKDIR /home/kip/src

# Copy project setup files
COPY --chown=kip:kip pyproject.toml .
COPY --chown=kip:kip poetry.lock .
COPY --chown=kip:kip README.md .

# Copy remaining files
COPY --chown=kip:kip Airlabs_api.py .

#######################################################################
# Test image
#######################################################################

FROM base as test

# Install the project locally for testing purposes
RUN poetry install


# Copy test files - not sure how to define pylintrc - T1
COPY --chown=kip:kip mypy.ini .
# COPY --chown=kip:kip .pylintrc .

# Copy test directory - once finished will uncomment it - T2
# COPY --chown=kip:kip test test

# Run tests as an entry point - once finished tox setup will uncomment it - T3
# ENTRYPOINT ["poetry", "run", "tox"]


#######################################################################
# Release image
#######################################################################

FROM base as release

# will uncomment after understand the docker-entrypoint - T4
# ENTRYPOINT ["poetry", "run", "./docker-entrypoint"]


