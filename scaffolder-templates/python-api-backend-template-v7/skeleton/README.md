# ${{values.component_id}}

${{values.description}}

# Namespaces 
There are three namespaces for this app in OpenShift:
- dev
- preprod 
- prod 

This application is deployed into different namespaces after following actions: 
- in dev by commit and push
- in pre-prod by setting tag 
- in prod by creating release
