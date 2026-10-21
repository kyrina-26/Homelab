# Homelab

A self-hosted homelab built to develop and demonstrate practical skills in Linux system administration, Docker, networking, security, and infrastructure management.

## Overview

This repository contains the infrastructure configuration, service definitions, custom integrations, and technical documentation for my homelab.

The environment runs on **Ubuntu Server**, using **Docker** and **Docker Compose** for containerized applications alongside native Linux services where appropriate.

The project emphasizes maintainable configurations, network security, service management, and practical self-hosting.

## Infrastructure

- **Operating System:** Ubuntu Server 26.04 LTS
- **Architecture:** `x86_64`
- **Container Platform:** Docker Engine
- **Orchestration:** Docker Compose
- **Reverse Proxy:** Nginx Proxy Manager
- **DNS:** Pi-hole
- **Remote Access:** Tailscale
- **Firewall:** UFW
- **File Sharing:** Samba

## Services

| Service | Purpose |
|---|---|
| **Nginx Proxy Manager** | Reverse proxy and TLS management |
| **Pi-hole** | DNS and network filtering |
| **Samba** | Authenticated network file sharing |
| **Cockpit** | Server administration |
| **Glances** | System and container monitoring |
| **Portainer** | Docker management |
| **Uptime Kuma** | Service availability monitoring |
| **Homarr** | Homelab dashboard |
| **Calibre** | Ebook library management and content serving |
| **Korest** | Self-hosted reading and synchronization services |
| **FlareSolverr** | Request-solving integration for supported sites |
| **Readest** | Ebook library access and management |

## Customizations

This repository also preserves selected application customizations and supporting utilities. See the individual service READMEs for implementation details and usage instructions, and consult the included license files for applicable licensing terms.

- **FanFicFare:** Customized Wattpad adapter with FlareSolverr compatibility.
- **Readest Sync:** Calibre plugin customizations for integration with a self-hosted Readest deployment.
- **Korest:** Utility for changing a user's password.
- **Environment examples:** Template configuration for supported services without committing actual environment secrets.

## Licensing

Original configurations, scripts, and documentation in this repository are licensed under the MIT License where applicable. See [LICENSE](LICENSE) for details.

Modified third-party software and other redistributed components retain their applicable upstream licenses and copyright notices. Refer to the relevant project READMEs and included license files for details.

