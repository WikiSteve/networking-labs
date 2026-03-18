# AWS Security Fundamentals

- Filename: `AWS Security Fundamentals.pptx`
- Subject: `cloud`
- Type: `lecture`
- Reusable: `yes`
- Source file: [Source copy](../../sources/AWS%20Security%20Fundamentals.pptx)

## Summary

This reusable lecture deck covers AWS security fundamentals through the shared-responsibility model, with a clear split between security of the cloud and security in the cloud. The first half focuses on AWS-managed responsibilities such as datacenter security, regional design, resiliency, compliance programs, media sanitization, audit artifacts, and the role of AWS Artifact in accessing compliance reports and agreements. The second half shifts to customer-side controls including IAM, credentials, Secrets Manager, STS, Directory Service, Organizations, Cognito, S3 encryption, CloudTrail, CloudWatch, AWS Config, VPC security controls, KMS versus CloudHSM, CloudFormation, incident-response automation with Step Functions, and DDoS protection using Shield, Route 53, and WAF.

## Key Details

- Introduces the AWS shared-responsibility model early and uses it as the organizing frame for the deck.
- Covers security of the cloud topics such as physical datacenter protection, environmental controls, backup power, HVAC, fire suppression, telecom infrastructure, resiliency testing, and address secrecy.
- Explains compliance in practical terms, including SOC, PCI DSS, ISO-style audits, data sovereignty, and AWS Artifact.
- Includes media-sanitization concepts from NIST SP 800-88 such as clear, purge, and destroy.
- Defines security in the cloud as the customer side of encryption, network controls, access control, service configuration, and compliance duties.
- Spends substantial time on IAM and credentials, including root versus limited IAM users, least privilege, access keys, EC2 key pairs, and API-driven access.
- Covers identity and secret-management services such as Secrets Manager, STS, Directory Service, Organizations, and Cognito.
- Explains data protection services including S3 server-side encryption, KMS, CloudHSM, FIPS 140-2 concepts, and the tradeoff between KMS and CloudHSM.
- Covers detective controls such as CloudTrail, CloudWatch, AWS Config, and related services like GuardDuty, Trusted Advisor, VPC Flow Logs, and Security Hub.
- Explains VPC security architecture including public and private subnets, route tables, internet gateways, security groups, and NACLs.
- Includes automation and operations topics such as Patch Manager, Parameter Store, Run Command, Session Manager, and CloudFormation.
- Ends with incident response and DDoS mitigation using Step Functions, Shield, Route 53, and WAF with TLS termination.

## Tags

- `aws-security`
- `shared-responsibility`
- `iam`
- `cloudtrail`
- `cloudwatch`
- `kms`
- `vpc-security`
- `ddos`
