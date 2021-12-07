
#!/bin/bash

echo "creating container"
docker build -t climber-test . 

echo "mounting" 
docker run -v "%cd%\RUN101":/usr/src/Climber/examples/RUN101 -it climber-test bash

#docker run -it climber-test bash

#cd /usr/src/Climber/examples/RUN101

#read state file




