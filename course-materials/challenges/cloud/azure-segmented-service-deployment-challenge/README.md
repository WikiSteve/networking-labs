# Azure Segmented Service Deployment Challenge

> **Before you start:** Download the [Azure Segmented Service Deployment Challenge Submission Template](<./assets/Azure Segmented Service Deployment Challenge SUBMISSION TEMPLATE.pptx>). Add each required screenshot directly into this file as you complete the lab, then submit the completed template for grading.

## Overview

A small startup needs a simple public-facing prototype deployed in Azure. The prototype must be reachable from the internet, but administrative access and an internal-only service must be restricted with Azure NSG rules.

You are not being graded as web developers. You are being graded on building the Azure resources and proving that your access policy works.

The public webpage is just the visible result. The real goal is to prove your access matrix works.

## What You Will Build

Create and configure the following:

- one resource group: `rg-firstname-practical`
- one virtual network: `vnet-firstname-practical`
- address space: `10.10.0.0/16`
- two subnets:
  - `server-subnet`: `10.10.1.0/24`
  - `client-subnet`: `10.10.2.0/24`
- one Ubuntu server VM such as `vm-firstname-server`
  - public IP
  - Nginx running on port `80`
  - one simple webpage hosted on Nginx
- one Ubuntu client VM such as `vm-firstname-client`
  - public IP
  - used to test internal access and SSH
- one NSG such as `nsg-firstname-server-segment` attached to the server subnet after the server services are configured

## Access Matrix

Your deployment must meet this policy:

| Source | TCP 80 | TCP 22 | TCP 8080 |
| --- | ---: | ---: | ---: |
| Internet | Allow | Deny | Deny |
| Client VM | Allow | Allow | Allow |

In plain English:

- the internet should only reach the public website on port `80`
- the client VM should be able to reach all three required ports on the server
- later in the NSG, you will add a broad deny for other VNet traffic so Azure's default allow behavior does not accidentally do the work for you

## Webpage Requirements

Your public page must include:

- a title
- a short description of the project
- one extra section, image, or second page
- some simple CSS styling

On the server VM, you will run:

- a public Nginx website on port `80`
- SSH on port `22`, allowed only from the client VM
- an internal-only service on port `8080`, allowed only from the client VM

For port `8080`, keep it simple. A Python `http.server` is enough.

The site is not the hard part. The access policy is.

## Pages

- [01 Before You Begin](01_before-you-begin.md)
- [02 Build Azure Resources](02_build-azure-resources.md)
- [03 Configure Server Services](03_configure-server-services.md)
- [04 Configure Server Subnet NSG](04_configure-server-subnet-nsg.md)
- [05 Validate and Prove](05_validate-and-prove.md)
- [06 Submission and Cleanup](06_submission-and-cleanup.md)
