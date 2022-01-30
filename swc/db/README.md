## Adding Persistant Volume PostgreSQL Container to Kubernetes
- Refer these links one by one: 
  - https://medium.com/@xcoulon/deploying-your-first-web-app-on-minikube-6e98d2884b3a
  - https://medium.com/@xcoulon/managing-pod-configuration-using-configmaps-and-secrets-in-kubernetes-93a2de9449be
  - https://medium.com/@xcoulon/storing-data-into-persistent-volumes-on-kubernetes-fb155da16666
- These values are base64 encoded and added to the secret yaml file.
`password: root`
- These are configuration files and added to the configmap yaml file.
`dbname: tourism` `username: postgres`.