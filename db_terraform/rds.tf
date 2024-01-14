#https://medium.com/strategio/using-terraform-to-create-aws-vpc-ec2-and-rds-instances-c7f3aa416133

resource "aws_db_instance" "db" {
  allocated_storage      = 10
  db_name                = "slots"
  engine                 = "postgres"
  instance_class         = "db.t3.micro"
  username               = "postgres"
  password               = "postgres"
  skip_final_snapshot    = true
  vpc_security_group_ids = ["${aws_security_group.rds_sg.id}"]
  db_subnet_group_name   = aws_db_subnet_group.rds_subnet_group.id
}
