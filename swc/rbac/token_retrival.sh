TOKEN=$(k describe secrets "$(k describe serviceaccount swc-pod-reader-sa -n swc-app| grep -i Tokens | awk '{print $2}')" -n swc-app | grep token: | awk '{print $2}'
