.PHONY: data data-clean test

data:
	mkdir Data
	curl -o ./Data/Datasheets_abilities.csv http://wahapedia.ru/wh40k10ed/Datasheets_abilities.csv
	curl -o ./Data/Datasheets_models_cost.csv http://wahapedia.ru/wh40k10ed/Datasheets_models_cost.csv
	curl -o ./Data/Datasheets_models.csv http://wahapedia.ru/wh40k10ed/Datasheets_models.csv
	curl -o ./Data/Datasheets_options.csv http://wahapedia.ru/wh40k10ed/Datasheets_options.csv
	curl -o ./Data/Datasheets_unit_composition.csv http://wahapedia.ru/wh40k10ed/Datasheets_unit_composition.csv
	curl -o ./Data/Datasheets_wargear.csv http://wahapedia.ru/wh40k10ed/Datasheets_wargear.csv
	curl -o ./Data/Datasheets.csv http://wahapedia.ru/wh40k10ed/Datasheets.csv
	curl -o ./Data/Factions.csv http://wahapedia.ru/wh40k10ed/Factions.csv

data-clean:
	rm -rf Data

test:
	python3 Lookup.py < blastTest.txt
