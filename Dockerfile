# STAGE 0: base image
FROM python:3.8-alpine AS base

LABEL author="Meysam Azad <MeysamAzad81@gmail.com>"

ARG WHEELDIR=/wheelhouse
ARG BUILDDIR=/build
ARG REQUIREMENTS=requirements.txt
ARG DUMB_INIT='https://github.com/Yelp/dumb-init/releases/download/v1.2.5/dumb-init_1.2.5_x86_64'
ARG ENV=DEVELOPMENT
ARG USER=medium
ARG SERVICEDIR=/home/${USER}
ARG PORT=8000
ARG APP_DIR=${SERVICEDIR}/app
ARG FILE_UPLOAD_PATH=/tmp/lware

ENV USER=${USER} \
    PORT=${PORT} \
    ENV=${ENV} \
    PYTHONUNBUFFERED=1 \
    BUILDDIR=${BUILDDIR} \
    WHEELDIR=${WHEELDIR} \
    REQUIREMENTS=${REQUIREMENTS}

RUN pip install -U pip && \
    apk add --update curl && \
    curl -sLo /usr/local/bin/dumb-init ${DUMB_INIT} && \
    chmod +x /usr/local/bin/dumb-init && \
    adduser -D ${USER}

# STAGE 1: fetch dependencies
FROM base AS build

COPY ${REQUIREMENTS} ${BUILDDIR}/
RUN pip wheel -r ${BUILDDIR}/${REQUIREMENTS} -w ${WHEELDIR}

# STAGE 2: ready to run the server
FROM base AS run

EXPOSE ${PORT}
WORKDIR ${SERVICEDIR}

COPY --from=build ${BUILDDIR} ${BUILDDIR}
COPY --from=build ${WHEELDIR} ${WHEELDIR}

RUN pip install ${WHEELDIR}/* && \
    rm -rf ${BUILDDIR} ${WHEELDIR}

COPY --chown=${USER} . .

USER ${USER}

ENTRYPOINT [ "/usr/local/bin/dumb-init", "--" ]
CMD ["./entrypoint.sh"]
