# AutoTag all EC2 instances
Date: 2022-08-08

This is a deploymoent package with Serverless Framework.

Configuration AutoTag all created EC2 instances with tag Creator and value of aws account username, who crated an EC2.

Read more about StackSets:
https://aws.amazon.com/blogs/aws/use-cloudformation-stacksets-to-provision-resources-across-multiple-aws-accounts-and-regions/

How to:
1. Go to AWS console -> CloudFormation.
2. From the top left side menu click on CloudFormation and choose a StackSets
3. Deploy the configuration on account and regions you need to.

For details how to implement StackSets please read an link above.


Author:
Łukasz Dorosz [@mrdoro](https://twitter.com/mrdoro)
