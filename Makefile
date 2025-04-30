.PHONY: clean all watch version generate

talk_slug := $(shell jq -r .talk_slug .cookiecutter.json)
talk_filename := $(shell ls ${talk_slug}.*)
latexmk := latexmk

all:
	${latexmk} ${talk_filename}

clean:
	latexmk -c

watch:
	${latexmk} ${talk_filename} -pvc 

view: 
	${latexmk} ${talk_filename} -pv


version: all
	theme/version.py ${talk_slug}

generate:
	theme/generate_head.py .cookiecutter.json > head.tex
