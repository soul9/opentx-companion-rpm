MOCK_RESULT_DIR := $(outdir)
MOCK_RESULT_DIR ?= "./results/%(dist)s/%(target_arch)s/"

ifndef srpm
	srpm := $(outdir)/*.src.rpm
endif
MOCK_SRPM := $(srpm)
ifndef spec
	spec := ./sources
endif
MOCK_SOURCESDIR := $(spec)

fetch:
	spectool -g -C $(MOCK_SOURCESDIR) $(MOCK_SOURCESDIR)/opentx-companion-2.2.1.spec

srpm:
	mock --buildsrpm --spec $(MOCK_SOURCESDIR)/opentx-companion-2.2.1.spec --sources $(MOCK_SOURCESDIR) --resultdir=$(MOCK_RESULT_DIR)

rpm: srpm
	mock --rebuild --resultdir=$(MOCK_RESULT_DIR) $(MOCK_SRPM)

clean:
	rm -rf $(MOCK_RESULT_DIR)

distclean:
	rm -rf $(MOCK_SOURCESDIR)/opentx-b55b68f.tar.gz

cleanall: clean distclean

all: rpm
