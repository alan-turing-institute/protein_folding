# A dockerfile must always start by importing the base image.
# We use the keyword 'FROM' to do that.
# In our example, we want import the python image.
# So we write 'python' for the image name and 'latest' for the version.
FROM ubuntu:latest

RUN apt-get -y update
RUN apt-get install python3 -y

# Install add 32 bit architecture in ubundu 
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 zlib1g:i386

# Install Cron
#RUN apt-get install cron -y && apt-get install vim -y
# Crontab file copied to cron.d directory.
#COPY cronjob /etc/cron.d/container_cronjob

# In order to launch our python code, we must import it into our image.
# We use the keyword 'COPY' to do that.
# The first parameter 'main.py' is the name of the file on the host.
# The second parameter '/' is the path where to put the file on the image.
# Here we put the file at the image root folder.
COPY Climber /usr/src/Climber
ENV CLIMBERDIR=/usr/src/Climber

# configures the container to run as an executable
#ENTRYPOINT ["/run.sh"]


#COPY config.sh /usr/src/


#RUN /usr/src/config.sh
#RUN bash /usr/src/config.sh

# COPY RUN101 /usr/src/Climber/examples/RUN101




# We need to define the command to launch when we are going to run the image.
# We use the keyword 'CMD' to do that.
# The following command will execute "python ./main.py".
# CMD [ "python", "./main.py" ]