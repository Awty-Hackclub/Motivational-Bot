sudo killall -q docker 
sudo docker build . -t bot
sudo docker run bot