FROM python:3-alpine

# Install required packages for building app dependencies
RUN apk add --no-cache \
    gcc \
    linux-headers \
    musl-dev \
    pcre-dev \
    postgresql-dev && \
    pip install --no-cache-dir uwsgi

RUN addgroup -S app && adduser -S -G app app

ARG LOG_BASE_DIR
ENV LOG_BASE_DIR=${LOG_BASE_DIR}
RUN mkdir -p ${LOG_BASE_DIR}

ARG APP_DIR
ENV APP_DIR=${APP_DIR}
WORKDIR ${APP_DIR}

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# USER app

ARG CONFIG_DIR
ENV CONFIG_DIR=${CONFIG_DIR}

COPY docker/scripts/setup-db.sh .
COPY conf/espn-ffb-docker.ini ${CONFIG_DIR}/espn-ffb.ini
COPY espn_ffb espn_ffb

EXPOSE 5000

CMD uwsgi --ini ${CONFIG_DIR}/espn-ffb.ini
