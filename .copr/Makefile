MOCK_RESULT_DIR := $(outdir)
MOCK_RESULT_DIR ?= "./results/%(dist)s/%(target_arch)s/"

MOCK_SRPM := $(srpm)
ifndef srpm
	MOCK_SRPM ?= $(outdir)/*.src.rpm
endif

MOCK_SOURCESDIR := $(spec)
ifndef spec
	MOCK_SOURCESDIR := ./sources
endif

distros := epel-7 fedora-26 fedora-27 fedora-28 fedora-rawhide
arches := x86_64 i386

fetch:
	spectool -g -C $(MOCK_SOURCESDIR) $(MOCK_SOURCESDIR)/opentx-companion-2.2.1.spec

srpm:
	mock --buildsrpm --spec=$(MOCK_SOURCESDIR)/opentx-companion-2.2.1.spec --sources=$(MOCK_SOURCESDIR) --resultdir=$(MOCK_RESULT_DIR)

dist: fetch srpm

rpm-%: srpm
	for arch in $(arches); do \
		echo mock --rebuild -r "$%"-"$$arch" --resultdir=$(MOCK_RESULT_DIR) $(MOCK_SRPM) ; \
	done

rpm-all: rpm-epel-7 rpm-fedora-26 rpm-fedora-27 rpm-fedora-28 rpm-fedora-rawhide

clean:
	rm -rf $(MOCK_RESULT_DIR)

distclean:
	rm -rf $(MOCK_SOURCESDIR)/opentx-b55b68f.tar.gz

cleanall: clean distclean

distall: dist rpm-all

all: rpm-all
