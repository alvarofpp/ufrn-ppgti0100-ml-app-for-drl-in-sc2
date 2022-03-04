FROM alvarofpp/s2client:4.9.3 AS sc2client

FROM python:3.9.10

# Install requirements
RUN pip3 install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY --from=sc2client /root/StarCraftII /root/StarCraftII

# Set environment variables
ENV WORKDIR=/app
WORKDIR ${WORKDIR}
