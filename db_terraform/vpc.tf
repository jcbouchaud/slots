# https://medium.com/@hmalgewatta/setting-up-an-aws-ec2-instance-with-ssh-access-using-terraform-c336c812322f

resource "aws_vpc" "vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = {
    Name = "rds-vpc"
  }
}

resource "aws_subnet" "ec2_sn1" {
  cidr_block        = "10.0.1.0/24"
  vpc_id            = aws_vpc.vpc.id
  availability_zone = "${var.region}a"
}

resource "aws_security_group" "ec2_sg" {
  name   = "ec2_sg"
  vpc_id = aws_vpc.vpc.id

  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 22
    to_port   = 22
    protocol  = "tcp"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_eip" "ec2_elastic_ip" {
  instance = aws_instance.ec2_rds.id
  domain   = "vpc"
}

resource "aws_internet_gateway" "ec2_gw" {
  vpc_id = aws_vpc.vpc.id
  tags = {
    Name = "gw"
  }
}

resource "aws_route_table" "ec2_rt" {
  vpc_id = aws_vpc.vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.ec2_gw.id
  }
  tags = {
    Name = "rt"
  }
}

resource "aws_route_table_association" "ec2_subnet-association" {
  subnet_id      = aws_subnet.ec2_sn1.id
  route_table_id = aws_route_table.ec2_rt.id
}

resource "aws_subnet" "rds_sn1" {
  cidr_block        = "10.0.101.0/24"
  vpc_id            = aws_vpc.vpc.id
  availability_zone = "${var.region}a"
}

resource "aws_subnet" "rds_sn2" {
  cidr_block        = "10.0.102.0/24"
  vpc_id            = aws_vpc.vpc.id
  availability_zone = "${var.region}b"
}

resource "aws_route_table" "rds_rt1" {
  vpc_id = aws_vpc.vpc.id

  tags = {
    Name = "rds_rt1"
  }
}

resource "aws_route_table_association" "rds_subnet-association_1" {
  subnet_id      = aws_subnet.rds_sn1.id
  route_table_id = aws_route_table.rds_rt1.id
}

resource "aws_route_table" "rds_rt2" {
  vpc_id = aws_vpc.vpc.id

  tags = {
    Name = "rds_rt2"
  }
}

resource "aws_route_table_association" "rds_subnet-association_2" {
  subnet_id      = aws_subnet.rds_sn2.id
  route_table_id = aws_route_table.rds_rt2.id
}

resource "aws_security_group" "rds_sg" {
  name   = "rds_sg"
  vpc_id = aws_vpc.vpc.id

  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.ec2_sg.id]
  }
}

resource "aws_db_subnet_group" "rds_subnet_group" {
  name       = "rds_subnet_group"
  subnet_ids = [aws_subnet.rds_sn1.id, aws_subnet.rds_sn2.id]
}
