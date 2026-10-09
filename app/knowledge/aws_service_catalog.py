AWS_SERVICE_CATALOG = {
    "amazon_s3": {
        "name": "Amazon S3",
        "category": "Storage",
        "description": (
            "Object storage for files, documents, images, "
            "backups, and application data."
        ),
        "aliases": [
            "S3",
            "Amazon Simple Storage Service",
            "Amazon S3",
            "Amazon Simple Storage Service (Amazon S3)",
        ],
        "icon": "s3.png",
        "diagram_supported": True,
    },

    "aws_lambda": {
        "name": "AWS Lambda",
        "category": "Compute",
        "description": (
            "Runs application code without managing servers."
        ),
        "aliases": [
            "Lambda",
            "AWS Lambda",
        ],
        "icon": "lambda.png",
        "diagram_supported": True,
    },

    "amazon_dynamodb": {
        "name": "Amazon DynamoDB",
        "category": "Database",
        "description": (
            "Fully managed NoSQL database for scalable applications."
        ),
        "aliases": [
            "DynamoDB",
            "Amazon DynamoDB",
        ],
        "icon": "dynamodb.png",
        "diagram_supported": True,
    },

    "amazon_api_gateway": {
        "name": "Amazon API Gateway",
        "category": "Application Integration",
        "description": (
            "Creates, publishes, secures, and manages APIs "
            "for applications."
        ),
        "aliases": [
            "API Gateway",
            "Amazon API Gateway",
        ],
        "icon": "api-gateway.png",
        "diagram_supported": True,
    },

    "amazon_cloudfront": {
        "name": "Amazon CloudFront",
        "category": "Networking & Content Delivery",
        "description": (
            "Content delivery network for delivering applications "
            "and content globally."
        ),
        "aliases": [
            "CloudFront",
            "Amazon CloudFront",
        ],
        "icon": "cloudfront.png",
        "diagram_supported": True,
    },

    "amazon_sns": {
        "name": "Amazon SNS",
        "category": "Application Integration",
        "description": (
            "Managed messaging and notification service."
        ),
        "aliases": [
            "SNS",
            "Amazon SNS",
            "Amazon Simple Notification Service",
            "Amazon Simple Notification Service (Amazon SNS)",
        ],
        "icon": "sns.png",
        "diagram_supported": True,
    },
    
    "amazon_cognito": {
        "name": "Amazon Cognito",
        "category": "Security, Identity, & Compliance",
        "description": (
            "Provides authentication, authorization, and user "
            "management for web and mobile applications."
        ),
        "aliases": [
            "Cognito",
            "Amazon Cognito",
        ],
        "icon": "cognito.png",
        "diagram_supported": True,
    },

    "amazon_sqs": {
        "name": "Amazon SQS",
        "category": "Application Integration",
        "description": (
            "Managed message queuing service for decoupling "
            "application components."
        ),
        "aliases": [
            "SQS",
            "Amazon SQS",
            "Amazon Simple Queue Service",
            "Amazon Simple Queue Service (Amazon SQS)",
        ],
        "icon": "sqs.png",
        "diagram_supported": True,
    },

    "amazon_eventbridge": {
        "name": "Amazon EventBridge",
        "category": "Application Integration",
        "description": (
            "Serverless event bus for connecting applications "
            "and reacting to events."
        ),
        "aliases": [
            "EventBridge",
            "Amazon EventBridge",
        ],
        "icon": "eventbridge.png",
        "diagram_supported": True,
    },

    "aws_step_functions": {
        "name": "AWS Step Functions",
        "category": "Application Integration",
        "description": (
            "Managed workflow service for coordinating distributed "
            "applications and processes."
        ),
        "aliases": [
            "Step Functions",
            "AWS Step Functions",
        ],
        "icon": "step-functions.png",
        "diagram_supported": True,
    },

    "amazon_rds": {
        "name": "Amazon RDS",
        "category": "Database",
        "description": (
            "Managed relational database service supporting "
            "multiple database engines."
        ),
        "aliases": [
            "RDS",
            "Amazon RDS",
            "Relational Database Service",
        ],
        "icon": "rds.png",
        "diagram_supported": True,
    },

    "amazon_aurora": {
        "name": "Amazon Aurora",
        "category": "Database",
        "description": (
            "Managed relational database engine compatible with "
            "MySQL and PostgreSQL."
        ),
        "aliases": [
            "Aurora",
            "Amazon Aurora",
        ],
        "icon": "aurora.png",
        "diagram_supported": True,
    },

    "amazon_ec2": {
        "name": "Amazon EC2",
        "category": "Compute",
        "description": (
            "Provides resizable compute capacity using virtual servers."
        ),
        "aliases": [
            "EC2",
            "Amazon EC2",
            "Elastic Compute Cloud",
        ],
        "icon": "ec2.png",
        "diagram_supported": True,
    },

    "amazon_ecs": {
        "name": "Amazon ECS",
        "category": "Containers",
        "description": (
            "Managed container orchestration service for running "
            "containerized applications."
        ),
        "aliases": [
            "ECS",
            "Amazon ECS",
            "Elastic Container Service",
        ],
        "icon": "ecs.png",
        "diagram_supported": True,
    },

    "amazon_eks": {
        "name": "Amazon EKS",
        "category": "Containers",
        "description": (
            "Managed Kubernetes service for running containerized "
            "applications."
        ),
        "aliases": [
            "EKS",
            "Amazon EKS",
            "Elastic Kubernetes Service",
        ],
        "icon": "eks.png",
        "diagram_supported": True,
    },

    "amazon_bedrock": {
        "name": "Amazon Bedrock",
        "category": "Machine Learning & AI",
        "description": (
            "Managed service providing access to foundation models "
            "for generative AI applications."
        ),
        "aliases": [
            "Bedrock",
            "Amazon Bedrock",
        ],
        "icon": "bedrock.png",
        "diagram_supported": True,
    },

    "amazon_opensearch_service": {
        "name": "Amazon OpenSearch Service",
        "category": "Analytics",
        "description": (
            "Managed search and analytics service for logs, search, "
            "and analytical workloads."
        ),
        "aliases": [
            "OpenSearch",
            "Amazon OpenSearch",
            "OpenSearch Service",
        ],
        "icon": "opensearch.png",
        "diagram_supported": True,
    },

    "aws_secrets_manager": {
        "name": "AWS Secrets Manager",
        "category": "Security, Identity, & Compliance",
        "description": (
            "Securely stores, manages, and retrieves application "
            "secrets such as database credentials and API keys."
        ),
        "aliases": [
            "Secrets Manager",
            "AWS Secrets Manager",
        ],
        "icon": "secrets-manager.png",
        "diagram_supported": True,
    },

    "aws_kms": {
        "name": "AWS Key Management Service",
        "category": "Security, Identity, & Compliance",
        "description": (
            "Creates and manages cryptographic keys used to "
            "protect data."
        ),
        "aliases": [
            "KMS",
            "AWS KMS",
            "Key Management Service",
            "AWS Key Management Service (AWS KMS)",
        ],
        "icon": "kms.png",
        "diagram_supported": True,
    },

    "aws_iam": {
        "name": "AWS Identity and Access Management",
        "category": "Security, Identity, & Compliance",
        "description": (
            "Controls access to AWS resources using users, roles, "
            "policies, and permissions."
        ),
        "aliases": [
            "IAM",
            "AWS IAM",
            "Identity and Access Management",
            "AWS Identity and Access Management (IAM)",
        ],
        "icon": "iam.png",
        "diagram_supported": True,
    },
        "amazon_vpc": {
        "name": "Amazon VPC",
        "category": "Networking & Content Delivery",
        "description": "Provides isolated virtual networking environments for AWS resources.",
        "aliases": [
            "VPC",
            "Amazon VPC",
            "Virtual Private Cloud",
        ],
        "icon": "vpc.png",
        "diagram_supported": True,
    },

    "aws_elastic_load_balancing": {
        "name": "Elastic Load Balancing",
        "category": "Networking & Content Delivery",
        "description": "Distributes incoming application traffic across multiple targets.",
        "aliases": [
            "ELB",
            "Elastic Load Balancer",
            "Load Balancer",
            "Elastic Load Balancing",
        ],
        "icon": "elastic-load-balancing.png",
        "diagram_supported": True,
    },

    "amazon_route_53": {
        "name": "Amazon Route 53",
        "category": "Networking & Content Delivery",
        "description": "Scalable DNS and domain name service for routing users to applications.",
        "aliases": [
            "Route 53",
            "Amazon Route 53",
            "Route53",
        ],
        "icon": "route-53.png",
        "diagram_supported": True,
    },

    "aws_waf": {
        "name": "AWS WAF",
        "category": "Security, Identity, & Compliance",
        "description": "Web application firewall that helps protect applications from common web exploits.",
        "aliases": [
            "WAF",
            "AWS WAF",
            "Web Application Firewall",
        ],
        "icon": "waf.png",
        "diagram_supported": True,
    },

    "amazon_cloudwatch": {
        "name": "Amazon CloudWatch",
        "category": "Management & Governance",
        "description": "Monitors applications, infrastructure, logs, metrics, and operational events.",
        "aliases": [
            "CloudWatch",
            "Amazon CloudWatch",
        ],
        "icon": "cloudwatch.png",
        "diagram_supported": True,
    },

    "aws_cloudtrail": {
        "name": "AWS CloudTrail",
        "category": "Management & Governance",
        "description": "Records AWS API activity for auditing, governance, and security analysis.",
        "aliases": [
            "CloudTrail",
            "AWS CloudTrail",
        ],
        "icon": "cloudtrail.png",
        "diagram_supported": True,
    },

    "aws_config": {
        "name": "AWS Config",
        "category": "Management & Governance",
        "description": "Tracks AWS resource configurations and evaluates them against desired rules.",
        "aliases": [
            "Config",
            "AWS Config",
        ],
        "icon": "config.png",
        "diagram_supported": True,
    },

    "amazon_elasticache": {
        "name": "Amazon ElastiCache",
        "category": "Database",
        "description": "Managed in-memory caching service for improving application performance.",
        "aliases": [
            "ElastiCache",
            "Amazon ElastiCache",
        ],
        "icon": "elasticache.png",
        "diagram_supported": True,
    },

    "amazon_kinesis": {
        "name": "Amazon Kinesis",
        "category": "Analytics",
        "description": "Processes and analyzes streaming data in real time.",
        "aliases": [
            "Kinesis",
            "Amazon Kinesis",
        ],
        "icon": "kinesis.png",
        "diagram_supported": True,
    },

    "amazon_ses": {
        "name": "Amazon SES",
        "category": "Application Integration",
        "description": "Cloud-based email service for sending transactional and bulk email.",
        "aliases": [
            "SES",
            "Amazon SES",
            "Amazon Simple Email Service",
            "Simple Email Service",
            "Amazon Simple Email Service (SES)",
            "Amazon Simple Email Service (Amazon SES)"
        ],
        "icon": "ses.png",
        "diagram_supported": True,
    },
    "amazon_textract": {
        "name": "Amazon Textract",
        "category": "Machine Learning & AI",
        "description": "Automatically extracts text, handwriting, and structured data from scanned documents and images.",
        "aliases": [
            "Textract",
            "Amazon Textract",
        ],
        "icon": "textract.png",
        "diagram_supported": True,
    },
        "aws_certificate_manager": {
        "name": "AWS Certificate Manager",
        "category": "Security, Identity, & Compliance",
        "description": "Manages SSL/TLS certificates for AWS services and applications.",
        "aliases": [
            "ACM",
            "AWS ACM",
            "AWS Certificate Manager",
            "Certificate Manager",
            "AWS Certificate Manager (ACM)",
        ],
        "icon": "certificate-manager.png",
        "diagram_supported": True,
    },
}