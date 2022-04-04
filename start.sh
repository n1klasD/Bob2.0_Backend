#!/usr/bin/env bash
sudo docker pull 1646552/controller:latest
sudo docker pull 1646552/welcome:latest
sudo docker pull 1646552/entertainment:latest
sudo docker pull 1646552/journey:latest
sudo docker pull 1646552/finances:latest
sudo docker-compose up
