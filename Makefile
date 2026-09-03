.PHONY: build test clean

build: clean
	mkdir -p _site
	cp -a website/. _site/

test: build
	python3 -m unittest discover -s tests

clean:
	rm -rf _site
