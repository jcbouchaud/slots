terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region     = "us-east-1"
  access_key = "LKIAQAAAAAAAH2MRTWGF"
  secret_key = "6DCn6aOm1nXlsfpoMUgB/PTSo4gekYClYcBzodcn"
}

