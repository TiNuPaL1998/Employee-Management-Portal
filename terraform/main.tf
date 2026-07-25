resource "aws_instance" "flask_server" {
  ami           = var.ami_id
  instance_type = var.instance_type

  key_name = "employee-management-key"

  vpc_security_group_ids = [
    aws_security_group.flask_sg.id
  ]

  tags = {
    Name = "Employee-Management-Portal"
  }
}