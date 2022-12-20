## Add your own custom Makefile targets here

RUN = poetry run
# is this really a schema generalization task? or a schema conversion-from template task?
#  the column headers in examples/basin3d_variables_hydrology.tsv are metadata,
#  and the row values are examples, so it is a generalization task

src/ess_dive_linkml_playground/schema/ess_dive_linkml_playground.yaml: examples/basin3d_variables_hydrology.tsv
	$(RUN) schemauto generalize-tsv \
		--output $@ $<