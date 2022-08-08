# AutoTag all EC2 instances
Date: 2022-08-08

This is a deploymoent package with Serverless Framework.

Configuration AutoTag all created EC2 instances with tag **Creator** and value of aws account username, who crated an EC2.

### How to:
1. Install a serverless framework with command:

```
npm install -g serverless 
```

2. Authenticate on your AWS Account. 

Check https://www.serverless.com/framework/docs/providers/aws/guide/credentials

3. Deploy it

```
serverless deploy
```

Author:
Łukasz Dorosz [@mrdoro](https://twitter.com/mrdoro)
