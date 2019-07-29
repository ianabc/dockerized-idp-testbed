# dockerized-idp-testbed

Used to validate the following Unicon docker images in a kubernetes setting:

- shibboleth-idp:
  [https://hub.docker.com/r/unicon/shibboleth-idp](https://github.com/Unicon/shibboleth-idp-dockerized).
- shibboleth-sp:
  [https://hub.docker.com/r/unicon/shibboleth-sp](https://github.com/Unicon/shibboleth-sp-dockerized).

More documentation is forthcoming, but it's a full working IDP, SP, and LDAP
server that runs under `kubernetes`. The included `docker-compose.yaml` is
mostly just for rebuilding the base images to include minor changes. If you are
interested in running this setup with docker-compose, see the original
[dockerized-idp-testbed](https://github.com/UniconLabs/dockerized-idp-testbed)
repository.

1. Run `docker-compose build` to build the images locally.
1. Tag the images and push them to a publicly accessible registry.
1. Create a namespace to hold things
   `$ kubectl create namespace idptest`
1. Create the kubernetes secrets (rebuild them with
   [./buildsecrets.py](./buildsecrets.py) as necessary)
   `$ kubectl -n idptest apply -f secrets.yaml`
1. Apply the ldap, idp, sp and httpd-proxy deployments and services.
   1. `$ kubectl -n idptest apply -f ldap-deployment.yaml`
   1. `$ kubectl -n idptest apply -f ldap-service.yaml`
   1. `$ kubectl -n idptest delete -f idp-deployment.yaml`
   1. `$ kubectl -n idptest apply -f idp-deployment.yaml`
   1. `$ kubectl -n idptest apply -f idp-service.yaml`
   1. `$ kubectl -n idptest apply -f sp-deployment.yaml`
   1. `$ kubectl -n idptest apply -f sp-service.yaml`
   1. `$ kubectl -n idptest apply -f httpd-proxy-deployment.yaml`
   1. `$ kubectl -n idptest apply -f httpd-proxy-service.yaml`
1. kubectl-forward ports 80 and 443 from localhost to the cluster
  `$ kubectl port-forward -n idptest svc/httpd-proxy 443:443 80:80` 
1. Browse to `https://idptestbed/` (after setting up an `etc/hosts` file entry
   pointing to your localhost), and you can login with `staff1` and `password`.

