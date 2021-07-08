#!/bin/bash

# start script in src/docker
cd ../../

# allocates ports
net stop winnat
netsh int ipv4 add excludedportrange protocol=tcp startport=50050 numberofports=1
netsh int ipv4 add excludedportrange protocol=tcp startport=50151 numberofports=1
netsh int ipv4 add excludedportrange protocol=tcp startport=50251 numberofports=1
netsh int ipv4 add excludedportrange protocol=tcp startport=50252 numberofports=1
netsh int ipv4 add excludedportrange protocol=tcp startport=50253 numberofports=1
net start winnat

# deletes the ServerInformation
printf '%.s-' {1..100}
printf " deletes ServerInformation Server "
printf '%.s-' {1..100}; echo "" 
docker stop serverInformation
docker rm serverInformation
docker rmi serverinformation

# deletes a router
printf '%.s-' {1..100}
printf " deletes Router Server "
printf '%.s-' {1..100}; echo ""
docker stop rendezvousHashing0
docker rm rendezvousHashing0
docker rmi rendezvoushashing0

# deletes a nodes
printf '%.s-' {1..100}
printf " deltes Node Servers "
printf '%.s-' {1..100}; echo ""
docker stop rendezvousNode0
docker stop rendezvousNode1
docker stop rendezvousNode2
docker rm rendezvousNode0
docker rm rendezvousNode1
docker rm rendezvousNode2
docker rmi rendezvousnode0
docker rmi rendezvousnode1
docker rmi rendezvousnode2

#starts the serverinformation
printf '%.s-' {1..100}
printf " creates and starts ServerInformation Server "
printf '%.s-' {1..100}; echo ""
docker build -t serverinformation -f src/Docker/Dockerfile_ServerInformation --build-arg PORT=50050 .
docker run -d -it --name serverInformation -p 50050:50050 serverinformation:latest 50050

# starts a router
printf '%.s-' {1..100}
printf " creates and starts Router Server "
printf '%.s-' {1..100}; echo ""
docker build -t rendezvoushashing0 -f src/Docker/Dockerfile_RenzRouter --build-arg PORT=50151 .
docker run -d -it --name rendezvousHashing0 -p 50151:50151 rendezvoushashing0:latest router0 50151

# starts a node
printf '%.s-' {1..100}
printf " creates and starts Node Servers "
printf '%.s-' {1..100}; echo ""
docker build -t rendezvousnode0 -f src/Docker/Dockerfile_RenzNode --build-arg PORT=50251 .
docker build -t rendezvousnode1 -f src/Docker/Dockerfile_RenzNode --build-arg PORT=50252 .
docker build -t rendezvousnode2 -f src/Docker/Dockerfile_RenzNode --build-arg PORT=50253 .
docker run -d -it --name rendezvousNode0 -p 50251:50251 rendezvousnode0:latest node0 50251 1.0
docker run -d -it --name rendezvousNode1 -p 50252:50252 rendezvousnode1:latest node1 50252 1.0
docker run -d -it --name rendezvousNode2 -p 50253:50253 rendezvousnode2:latest node2 50253 1.1

printf '%.s-' {1..100}
printf " done "
printf '%.s-' {1..100}; echo ""