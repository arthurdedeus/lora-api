provider "aws" {
  version = "~>2.0"
  region  = "us-east-1"
}

terraform {
  backend "s3" {
    bucket  = "<bucket-name>"
    key     = "terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}

locals {
  project         = "<project-name>"
  region          = "us-east-1"
  certificate_arn = "<certificate-arn>"
  instance_type   = "t2.micro"
  key_name        = "<keyname>"

  staging_db_config = {
    instance_class    = "db.t2.micro"
    allocated_storage = 5
    delete_protection = false
  }

  prod_db_config = {
    instance_class    = "db.t2.micro"
    allocated_storage = 5
    delete_protection = true
  }

  db_configs_all = {
    "staging" : local.staging_db_config,
    "prod" : local.prod_db_config,
  }
  db_config = lookup(local.db_configs_all, terraform.workspace, "staging")
}


resource "aws_s3_bucket" "env_bucket" {
  bucket = "${local.project}-backend-envs"
  acl    = "private"
}

module "vpc" {
  source  = "./VPC"
  project = local.project
}

module "alb" {
  source             = "./ALB"
  project            = local.project
  vpc_id             = module.vpc.this_vpc_id
  security_group_ids = [module.vpc.elb_security_group_id]
  subnet_ids         = module.vpc.this_subnet_ids
  certificate_arn    = local.certificate_arn
}

module "ecs" {
  source              = "./ECS"
  project             = local.project
  lb_target_group_arn = module.alb.this_target_group_arn
  security_group_ids  = [module.vpc.instances_security_group_id]
  subnet_ids          = module.vpc.this_subnet_ids
  instance_type       = local.instance_type
  region              = local.region
  key_name            = local.key_name
}

resource "random_string" "password" {
  length           = 16
  special          = true
  override_special = "!#$%&*-_=+[]{}<>"
}

module "rds" {
  source = "./RDS"

  project                = local.project
  instance_class         = local.db_config.instance_class
  allocated_storage      = local.db_config.allocated_storage
  delete_protection      = local.db_config.delete_protection
  name                   = local.project
  username               = "postgres"
  password               = random_string.password.result
  vpc_security_group_ids = [module.vpc.rds_security_group_id]
  subnet_ids             = module.vpc.this_subnet_ids
}
