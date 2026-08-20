# ML Infrastructure as Code (MLOps IaC)

## Description

Terraform, Pulumi, and GitOps for reproducible ML platforms, modular MLOps stacks, and CI/CD-managed infrastructure.

## When to use

You want to provision, version, and reproduce ML environments, pipelines, and serving infrastructure through code rather than manual setup.

## Key concepts

- **Infrastructure as Code (IaC)**: Terraform, Pulumi, AWS CDK, Azure Bicep.
- **GitOps**: infrastructure changes via Git pull requests and automated reconciliation.
- **MLOps platforms**: training, registry, serving, feature store, experiment tracking.
- **Modular stacks**: reusable components for data, compute, model registry, and monitoring.
- **State management and secrets**: remote state, locking, and secret injection.

## Code pattern

```hcl
# main.tf - Terraform snippet for MLOps base infrastructure
terraform {
  required_providers { aws = { source = "hashicorp/aws" } }
}

resource "aws_s3_bucket" "ml_artifacts" {
  bucket = "my-ml-artifacts-bucket"
}

resource "aws_sagemaker_notebook_instance" "nb" {
  name          = "mlops-notebook"
  role_arn      = aws_iam_role.sagemaker.arn
  instance_type = "ml.t3.medium"
  lifecycle_config_name = aws_sagemaker_notebook_lifecycle_configuration.setup.name
}
```

## Tuning notes

- Keep modules small, composable, and environment-agnostic.
- Use remote state with locking (e.g., S3 + DynamoDB) for team workflows.
- Parameterize instance types, regions, and cost settings per environment.
- Apply least-privilege IAM and network policies from the start.

## Verification

1. Define and deploy a minimal IaC stack for an S3 bucket and a compute instance.
2. Modify the stack via a PR and verify automated plan/apply in a staging environment.
3. Tear down and recreate the stack, confirming reproducibility and identical outputs.

## References

- https://aws.amazon.com/blogs/machine-learning/implement-a-secure-mlops-platform-based-on-terraform-and-github/
- https://github.com/aws-samples/mlops-multi-account-terraform
- https://github.com/zenml-io/mlstacks
- https://github.com/aws-samples/amazon-eks-machine-learning-with-terraform-and-kubeflow
- https://github.com/teamdatatonic/vertex-pipelines-end-to-end-samples
