## This repo contains a Django Application that is used to query the squad list of the various teams participating in the English Premier League 2023-2024 Season.

![Screenshot from 2024-01-21 21-17-28](https://github.com/nugowe/EPLPlayerListTable/assets/25004712/848e0848-6c03-4e3e-9a62-6658881402a6)

### BASIC USAGE:
Simply check the boxes of your favorite Team and the entire squad list for this season would appear. Technically, it involves using a form to send a queryset to query a database at the backend.

The query set is then rendered in the div section of the webpage for the App users consumption.

## WITHOUT THE CONTAINER  | VIA MAKEFILE

## DEPLOY THE SQUADLIST APP VIA DJANGO DIRECTLY....

Simply run the command:

make DEPLOY-SQUADLIST-LOCALLY

## DEPLOY THE SQUADLIST APP ON TO A KUBERNETES CLUSTER (MICROK8S IN MY CASE)

Simply run the command:

make DEPLOY-SQUADLIST-K8s


## PORT-FORWARD THE EPLSQUADLIST APP TO A WEB BROWSER (TO BE USED WHEN DEPLOY IN A KUBERNETES CLUSTER)

Simply run this command:

make PORT-FORWARD-SQUADLIST-K8s
