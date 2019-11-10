include config.mk
GENERATED_FILES= ./output/republicans.csv ./output/democrats.csv

.PHONY: all clean


./output/republicans.csv: legislators.table
	sql2csv --db $(FULL_POSTGRES_PATH) --query "SELECT * FROM legislators WHERE party = 'R' AND youtube_url IS NOT NULL AND facebook_id IS NOT NULL" > $@

./output/democrats.csv: legislators.table
	sql2csv --db $(FULL_POSTGRES_PATH) --query "SELECT * FROM legislators WHERE party = 'D' AND EXTRACT(YEAR FROM AGE(birthdate)) <= 45" > $@

legislators.table: ./raw/legislators.csv
	echo "SELECT 'CREATE DATABASE $(PG_DB)' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$(PG_DB)')\gexec" | psql
	psql -d $(PG_DB) -U $(PG_USER) -h $(PG_HOST) -p $(PG_PORT) -c "DROP TABLE IF EXISTS $(TABLE_NAME)"
	csvsql --db $(FULL_POSTGRES_PATH) --table $(TABLE_NAME) --insert $<
	touch $@

# Run all targets
all: $(GENERATED_FILES)
	dropdb $(PG_DB)
	rm legislators.table

# Remove all generated targets
clean:
	rm -rf output/*


