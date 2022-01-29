## Installing and Verifying Certificates in browser for HTTPS connection

- https://stackoverflow.com/questions/7580508/getting-chrome-to-accept-self-signed-localhost-certificate/60516812#60516812
- Domain name: `swc26.com` `api.swc26.com`
- Add these domain names to `/etc/hosts`:
- ```commandline
  127.0.0.1       localhost swc26.com api.swc26.com
  ```
- Finally Kubernetes secret needs to be configured for the TLS setting as shown in: https://kubernetes.io/docs/concepts/configuration/secret/#tls-secrets
- ```yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: secret-tls
    type: kubernetes.io/tls
    data:
    # the data is abbreviated in this example
      tls.crt: |
        MIIC2DCCAcCgAwIBAgIBATANBgkqh ...
      tls.key: |
        MIIEpgIBAAKCAQEA7yn3bRHQ5FHMQ ...
  ```
  or
  ```commandline
    kubectl create secret tls my-tls-secret \
  --cert=path/to/cert/file \
  --key=path/to/key/file
  ```
- The application required secret-tls yaml file is given here.
- Also for more reference: https://cloud.google.com/kubernetes-engine/docs/how-to/ingress-multi-ssl