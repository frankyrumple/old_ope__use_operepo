FROM nginx:1.11.3

# ope-gateway  - Open Prison Education gateway device
# Build: Follow instructions at https://github.com/frankyrumple/ope

LABEL maintainer="Ray Pulsipher <ray@cmagic.biz>"
LABEL description="Web Gateway for Open Prison Education - source files at https://github.com/operepo"
LABEL vendor="openprisoneducation.com"
LABEL version="0.5"

ARG VERSION=dev
ENV VIRTUAL_HOST=gateway.ed

# Fix encoding issues
#ENV LANG=en_US.UTF-8
ENV LANG=C.UTF-8
ENV TERM=xterm


# Install wget and install/updates certificates
RUN apt-get update \
 && apt-get install -y -q --no-install-recommends \
    ca-certificates \
    wget \
	nano \
	openssl \
 && apt-get clean \
 && rm -r /var/lib/apt/lists/*

 # Configure Nginx and apply fix for very long server names
RUN echo "daemon off;" >> /etc/nginx/nginx.conf \
 && sed -i 's/^http {/&\n    server_names_hash_bucket_size 128;/g' /etc/nginx/nginx.conf

# Install Forego
#ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego /usr/local/bin/forego
COPY forego /usr/local/bin/forego
RUN chmod u+x /usr/local/bin/forego

ENV DOCKER_GEN_VERSION 0.7.3

RUN wget https://github.com/jwilder/docker-gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && tar -C /usr/local/bin -xvzf docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz \
 && rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz

LABEL rebuild=12
RUN mkdir -p /app
#COPY fogserver.conf /etc/nginx/conf.d/
COPY docker-entrypoint.sh /app/
COPY nginx.tmpl /app/
COPY forego /app/
COPY Procfile /app/
WORKDIR /app/
RUN chmod +x /app/docker-entrypoint.sh

# Set upload params higher
RUN { \
      echo 'server_tokens off;'; \
      echo 'client_max_body_size 1000m;'; \
    } > /etc/nginx/conf.d/uploads.conf

ENV DOCKER_HOST unix:///tmp/docker.sock

VOLUME ["/etc/nginx/certs", "/tmp/docker.sock"]

EXPOSE 80 443

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["forego", "start", "-r"]

