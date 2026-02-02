# Makefile for PEARC'26 manuscript
# Uses latexmk for LaTeX compilation with build artifacts isolated to build/

# Project configuration
MAIN     := manuscript
BUILDDIR := build
AUTHOR   := lentner

# Commands
LATEXMK  := latexmk
OPEN     := open -a Skim

# latexmk flags
LATEXMK_FLAGS := -pdf -bibtex -output-directory=$(BUILDDIR) -aux-directory=$(BUILDDIR)

# Release filename: lentner-2026-{version}.pdf
# For local builds, uses latest tag; CI uses the release tag directly
DATE     := $(shell date +"%Y")
VERSION  := $(shell git describe --tags --abbrev=0 2>/dev/null | sed 's/^v//' || echo "dev")
RELEASE  := $(AUTHOR)-$(DATE)-$(VERSION).pdf

.PHONY: all build release watch open clean distclean builddir

# Default target
all: build

# Incremental build
build: builddir
	cp references.bib $(BUILDDIR)/
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

# Full clean rebuild for release
release: clean builddir
	cp references.bib $(BUILDDIR)/
	$(LATEXMK) $(LATEXMK_FLAGS) -gg $(MAIN).tex
	cp $(BUILDDIR)/$(MAIN).pdf ./$(RELEASE)
	@echo "Release created: $(RELEASE)"

# Continuous build with file watching (use Skim's built-in refresh)
watch: builddir
	$(LATEXMK) $(LATEXMK_FLAGS) -pvc $(MAIN).tex

# Open PDF in Skim
open:
	@if [ -f $(BUILDDIR)/$(MAIN).pdf ]; then \
		$(OPEN) $(BUILDDIR)/$(MAIN).pdf; \
	else \
		echo "PDF not found. Run 'make build' first."; \
		exit 1; \
	fi

# Clean build artifacts (keep release PDFs)
clean:
	$(LATEXMK) -output-directory=$(BUILDDIR) -C $(MAIN).tex 2>/dev/null || true
	/bin/rm -rf $(BUILDDIR)

# Clean everything including release PDFs
distclean: clean
	rm -f $(AUTHOR)-*.pdf

# Create build directory if it doesn't exist
builddir:
	@mkdir -p $(BUILDDIR)
