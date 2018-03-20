MOCK_RESULT_DIR := $(outdir)
MOCK_RESULT_DIR ?= "./results/%(dist)s/%(target_arch)s/"

MOCK_SRPM := $(srpm)
MOCK_SRPM ?= $(outdir)/*.src.rpm

MOCK_SOURCESDIR := $(spec)
MOCK_SOURCESDIR ?= ./sources

MOCK := $(shell command -v mock 2> /dev/null)

fetch:
	spectool -g -C $(MOCK_SOURCESDIR) $(MOCK_SOURCESDIR)/opentx-companion-2.2.1.spec

srpm:
ifndef MOCK
	yum -y install mock
endif
	mock --buildsrpm --spec=$(MOCK_SOURCESDIR)/opentx-companion-2.2.1.spec --sources=$(MOCK_SOURCESDIR) --resultdir=$(MOCK_RESULT_DIR)

rpm: srpm
	mock --rebuild --resultdir=$(MOCK_RESULT_DIR) $(MOCK_SRPM)

clean:
	rm -rf $(MOCK_RESULT_DIR)

distclean:
	rm -rf $(MOCK_SOURCESDIR)/opentx-b55b68f.tar.gz

cleanall: clean distclean

all: rpm
