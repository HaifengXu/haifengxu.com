HUGO ?= hugo

.PHONY: dev build new clean

dev:
	$(HUGO) server -D

build:
	$(HUGO) --gc --minify

new:
	@test -n "$(slug)" || (echo "Usage: make new slug=my-post" && exit 1)
	$(HUGO) new posts/$(slug).md

clean:
	rm -rf public resources .hugo_build.lock
