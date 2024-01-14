resource "tls_private_key" "private_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "ec2_key_pair" {
  key_name   = "ec2_key_pair"
  public_key = tls_private_key.private_key.public_key_openssh
}

resource "aws_secretsmanager_secret" "ec2_secret" {
  name = "ec2_secret"
}

resource "aws_secretsmanager_secret_version" "secret_version" {
  secret_id     = aws_secretsmanager_secret.ec2_secret.id
  secret_string = tls_private_key.private_key.private_key_pem
}

resource "aws_instance" "ec2_rds" {
  ami             = "ami-0005e0cfe09cc9050"
  instance_type   = "t2.micro"
  key_name        = aws_key_pair.ec2_key_pair.key_name
  security_groups = ["${aws_security_group.ec2_sg.id}"]
  subnet_id       = aws_subnet.ec2_sn1.id

  user_data = <<-EOF
              #!/bin/bash
              sudo dnf install -y postgresql15.x86_64
              EOF

  tags = {
    Name = "ec2-database-connect"
  }
}
