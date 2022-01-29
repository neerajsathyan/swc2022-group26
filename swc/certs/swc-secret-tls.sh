#!/bin/bash
kubectl create secret tls swc-secret-tls \
    --cert=swc26.com.crt \
    --key=swc26.com.key