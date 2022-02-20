FROM mcr.microsoft.com/mssql/server:2019-latest

# Create non-root user and update permissions
#
USER root

#RUN useradd -M -s /bin/bash -u 10001 -g 0 mssql
RUN mkdir -p -m 770 /var/opt/mssql && chgrp -R 0 /var/opt/mssql

# Grant sql the permissions to connect to ports <1024 as a non-root user
#
RUN setcap 'cap_net_bind_service+ep' /opt/mssql/bin/sqlservr

# Allow dumps from the non-root process
# 
RUN setcap 'cap_sys_ptrace+ep' /opt/mssql/bin/paldumper
RUN setcap 'cap_sys_ptrace+ep' /usr/bin/gdb

# Add an ldconfig file because setcap causes the os to remove LD_LIBRARY_PATH
# and other env variables that control dynamic linking
#
RUN mkdir -p /etc/ld.so.conf.d && touch /etc/ld.so.conf.d/mssql.conf
RUN echo -e "# mssql libs\n/opt/mssql/lib" >> /etc/ld.so.conf.d/mssql.conf
RUN ldconfig








ENV ACCEPT_EULA=Y
ENV MSSQL_PID=Developer
ENV MSSQL_SA_PASSWORD='<sApassword>'
ENV MSSQL_TCP_PORT=1422

EXPOSE 1422

WORKDIR /src

COPY sql_files/db_backup.sql ./db_backup.sql
COPY sql_files/db_restore.sql ./db_restore.sql


USER mssql
RUN echo "BEFORE STARTING SERVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1"
RUN /opt/mssql/bin/sqlservr --accept-eula &
RUN echo "AFTER STARTING SERVER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

CMD  (/opt/mssql-tools/bin/sqlcmd -b -S 127.0.0.1,1433 -U sa -P '<sapassword>' -i db_backup.sql) \
       && (echo "PING!") \
#&& (/opt/mssql-tools/bin/sqlcmd -b -S localhost,1422 -U sa -P '<sApassword>' -i db_restore.sql) \
       && (echo "PONG!") \
       && (tail -f /dev/null)


