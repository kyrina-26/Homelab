# Homelab

A self-hosted homelab built to develop and demonstrate practical skills in Linux system administration, Docker, networking, security, and infrastructure management.

## Overview

This repository contains the infrastructure configuration, service definitions, and technical documentation for my homelab.

The environment runs on **Ubuntu Server**, using **Docker** as the primary platform for containerized services alongside native Linux services where appropriate.

## Infrastructure

* **Operating System:** Ubuntu Server 26.04 LTS
* **Architecture:** `x86_64`
* **Container Platform:** Docker Engine
* **Orchestration:** Docker Compose
* **Reverse Proxy:** Nginx Proxy Manager
* **DNS:** Pi-hole
* **Remote Access:** Tailscale
* **Firewall:** UFW
* **File Sharing:** Samba

## Services

| Service                 | Purpose                            |
| ----------------------- | ---------------------------------- |
| **Nginx Proxy Manager** | Reverse proxy and TLS              |
| **Pi-hole**             | DNS and network filtering          |
| **Samba**               | Authenticated network file sharing |
| **Cockpit**             | Server administration              |
| **Glances**             | System and container monitoring    |
| **Portainer**           | Docker management                  |
| **Uptime Kuma**         | Service availability monitoring    |
| **Homarr**              | Homelab dashboard                  |
