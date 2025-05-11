docker build -t scriitori_elena .
docker images
docker run -d -p 5000:5000 --name scriitori_elena_container scriitori_elena
