FROM registry.access.redhat.com/ubi8/python-38
ENV GIT_SSL_NO_VERIFY 1
WORKDIR /opt/app-root/src
COPY assets /opt/app-root/src/assets
COPY bonkify /opt/app-root/src/bonkify
COPY j2 /opt/app-root/src/j2
COPY Pipfile* /opt/app-root/src/
RUN pip3 install pipenv
RUN pipenv requirements > requirements.txt
RUN pip3 install -Ur requirements.txt
CMD ["python", "-m", "bonkify.server"]
