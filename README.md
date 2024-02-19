docker run -d \
	--name instsite_db \
	-e POSTGRES_PASSWORD=q1w2e3R$ \
	-e POSTGRES_USER=USER \
	-e POSTGRES_DB=instsite \
	-p 5432:5432 \
	postgres:15.0-alpine