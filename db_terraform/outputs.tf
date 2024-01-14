output "ec2_public_dns" {
  value      = aws_eip.ec2_elastic_ip.public_dns
  depends_on = [aws_eip.ec2_elastic_ip]
}

output "db_address" {
  value = aws_db_instance.db.address
}

