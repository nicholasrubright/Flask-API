FROM postgres:15.3-alpine
COPY ./init.sql /docker-entrypoint-initdb.d/init.sql
CMD ["docker-entrypoint.sh", "postgres"]