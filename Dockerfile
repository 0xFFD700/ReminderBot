FROM debian:buster

WORKDIR /opt/reminder

# install dependencies
RUN apt-get update \
    && apt-get install -y busybox-static python3 default-jre-headless \
    && rm -rf /var/lib/apt/lists/* \
    && busybox --install -s

# install signal-cli: https://github.com/AsamK/signal-cli
RUN wget https://github.com/AsamK/signal-cli/releases/download/v0.8.1/signal-cli-0.8.1.tar.gz
RUN tar xf signal-cli-0.8.1.tar.gz -C /opt
RUN ln -sf /opt/signal-cli-0.8.1/bin/signal-cli /usr/local/bin/

# set up cron job (every day at 16:00)
RUN mkdir -p /var/spool/cron/crontabs
RUN echo "0 16 * * * cd /opt/reminder && python3 reminder.py" | crontab -

COPY . .

VOLUME "/opt/reminder/reminder.csv" "/root/.local/share/signal-cli/data"
CMD crond -f -L /dev/stdout
