#!/bin/bash
images=(kube-proxy:v1.12.2 kube-scheduler:v1.12.2 kube-controller-manager:v1.12.2 kube-apiserver:v1.12.2 etcd:3.2.24 coredns:1.2.2 pause:3.1 ) 
for imageName in ${images[@]} ; do 
docker pull anjia0532/google-containers.$imageName 
docker tag anjia0532/google-containers.$imageName k8s.gcr.io/$imageName 
docker rmi anjia0532/google-containers.$imageName 
done
