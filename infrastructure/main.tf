provider "aws" {
  version = "~>2"
  region  = "us-east-1"
}

terraform {
  backend "s3" {
    bucket  = "boilerplate-backend-terraform"
    key     = "terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
}

locals {
  project         = "boilerplate"
  region          = "us-east-1"
  certificate_arn = "" #TODO: Your certificate ARN here
  keypair         = "boilerplate-keypair"

  staging_config = {
    ec2_instance_type    = "t2.micro"
    db_instance_class    = "db.t2.micro"
    db_allocated_storage = 5
    db_delete_protection = false
    storage_cdn_domain = [
      "images-staging.boilerplate.com",
    ]
#<celery>
    redis_node_type            = "cache.t2.micro"
    redis_num_cache_nodes      = 0
    redis_engine_version       = "5.0.5"
    redis_parameter_group_name = "default.redis5.0"
#</celery>
  }

  prod_config = {
    ec2_instance_type    = "t2.micro"
    db_instance_class    = "db.t2.micro"
    db_allocated_storage = 5
    delete_protection    = true
    storage_cdn_domain = [
      "images.boilerplate.com",
    ]
#<celery>
    redis_node_type            = "cache.t2.micro"
    redis_num_cache_nodes      = 0
    redis_engine_version       = "5.0.5"
    redis_parameter_group_name = "default.redis5.0"
#</celery>
  }

  configs = {
    "staging" : local.staging_config,
    "prod" : local.prod_config,
  }
  config = lookup(local.configs, terraform.workspace, "staging")
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
  instance_type       = local.config.ec2_instance_type
  region              = local.region
  key_name            = local.keypair
}

resource "random_string" "password" {
  length           = 16
  special          = false
  override_special = "!#$%&*-_=+[]{}<>"
}

module "rds" {
  source                 = "./RDS"
  project                = local.project
  instance_class         = local.config.db_instance_class
  allocated_storage      = local.config.db_allocated_storage
  delete_protection      = local.config.db_delete_protection
  name                   = local.project
  username               = "root"
  password               = random_string.password.result
  vpc_security_group_ids = [module.vpc.rds_security_group_id]
  subnet_ids             = module.vpc.this_subnet_ids
}

module "storage" {
  source          = "./Storage"
  project         = local.project
  cdn_domain      = local.config.storage_cdn_domain
  certificate_arn = local.certificate_arn
}
#<celery>
module "redis" {
  source               = "./Redis"
  project              = local.project
  node_type            = local.config.redis_node_type
  num_cache_nodes      = local.config.redis_num_cache_nodes
  engine_version       = local.config.redis_engine_version
  parameter_group_name = local.config.redis_parameter_group_name
  subnet_ids           = module.vpc.this_subnet_ids
  security_group_ids   = [module.vpc.redis_security_group_id]
}
#</celery>
