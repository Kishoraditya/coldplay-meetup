# Using free tier resources only

provider "aws" {
  region = "ap-south-1"
  
  # Free tier eligible
  default_tags {
    tags = {
      Project = "coldplay-meetup"
    }
  }
}

# EC2 t2.micro (free tier)
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y docker.io
              systemctl start docker
              systemctl enable docker
              EOF
  
  tags = {
    Name = "coldplay-meetup"
  }
}

# Using SQLite instead of RDS to stay free
# Using local Redis instead of ElastiCache
