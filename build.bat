aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 541445979751.dkr.ecr.ap-south-1.amazonaws.com
docker build -t labs_stt .
docker tag labs_stt:latest 541445979751.dkr.ecr.ap-south-1.amazonaws.com/labs_stt:latest