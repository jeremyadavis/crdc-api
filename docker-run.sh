#! /bin/bash
docker run -d -p 8080:8080 \
       -v /Users/jdavis/Sites/crdc_api/data/migrations:/hasura-migrations \
       -e HASURA_GRAPHQL_DATABASE_URL=postgres://postgres:@host.docker.internal:5432/postgres \
       -e HASURA_GRAPHQL_ENABLE_CONSOLE=true \
       hasura/graphql-engine:v1.0.0-alpha38.cli-migrations