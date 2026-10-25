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
| **Readest** | Ebook library management with an integrated reader |
| **Navidrome** | Self-hosted music streaming server |
| **Feishin** | Music streaming client for Navidrome |

## Installation and Deployment

This repository is organized around the configuration and management of individual services. Deployment requirements vary by service, so review the relevant configuration and documentation before starting a deployment.

### Prerequisites

- A Linux server or compatible environment with the resources required by the intended services.
- Git for cloning the repository.
- Docker Engine and the Docker Compose plugin for containerized services.
- Any additional dependencies specified in the relevant service documentation.

### Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/kyrina-26/Homelab.git
   ```

2. Navigate to the folder containing the service you want to deploy.

3. Review the service's README and Compose configuration to understand its requirements, dependencies, ports, volumes, and networking.

4. Configure the service's environment variables using the provided example configuration, where applicable. Supply your own values and keep actual secrets out of version control.

5. Prepare the required host directories, Docker networks, permissions, and other dependencies specified by the service configuration.

6. From the appropriate folder, deploy the service using Docker Compose:

   ```bash
   docker compose up -d
   ```

   Run this command only after reviewing and configuring the relevant Compose file and satisfying its prerequisites.

7. Verify the deployment using the service's logs, health checks, and documented access method.

### Important Notes

- **Deployment is service-specific.** Not every service can be deployed independently; some rely on shared networks, other services, or host-level configuration.
- **Host configuration may be required.** DNS, firewall rules, reverse proxy settings, file-sharing permissions, and native Linux services may require additional setup outside Docker Compose.
- **Review before exposing services.** Configure access controls, firewall rules, and reverse proxy settings appropriately before making services accessible over a network or the internet.
- **Protect sensitive information.** Example environment files are templates, not ready-to-use production credentials. Never commit real secrets or private configuration values.
- **Consult service documentation.** Refer to the individual service READMEs for specific installation, configuration, and maintenance instructions.

## Customizations

This repository also preserves selected application customizations and supporting utilities. See the individual service READMEs for implementation details and usage instructions, and consult the included license files for applicable licensing terms.

- **FanFicFare:** Customized Wattpad adapter with FlareSolverr compatibility.
- **Readest Sync:** Calibre plugin customizations for integration with a self-hosted Readest deployment.
- **Korest:** Utility for changing a user's password.
- **Environment examples:** Template configuration for supported services without committing actual environment secrets.

## Licensing

Original configurations, scripts, and documentation in this repository are licensed under the MIT License where applicable. See [LICENSE](LICENSE) for details.

Modified third-party software and other redistributed components retain their applicable upstream licenses and copyright notices. Refer to the relevant project READMEs and included license files for details.

