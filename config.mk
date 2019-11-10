# Please change these for your local Postgresql server
PG_HOST=localhost
PG_USER=elliotgoldingfrank
PG_PORT=5432

# These variables can remain the same - in the main Makefile
# we create a new PostgresDB and Table

PG_DB=sunlight
TABLE_NAME=legislators
FULL_POSTGRES_PATH=postgresql://$(PG_USER):@$(PG_HOST):$(PG_PORT)/$(PG_DB)
