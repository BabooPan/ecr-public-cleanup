# Image Cleanup for ECR Public

Inspired by [awslabs/ecr-cleanup-lambda](https://github.com/awslabs/ecr-cleanup-lambda)

ECR supports [Life policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) for private repository, but ECR public. The Python script help clean up untagged images in ECR public. The script looks for images that are not used & tagged in ECT public repositories that can be deleted.

## Authenticate with AWS

[Configuring the AWS Command Line Interface.](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html)
