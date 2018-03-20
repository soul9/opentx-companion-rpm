MOCK_RESULT_DIR := $(outdir)
MOCK_SRPM_RESULT_DIR := $(outdir)
ifndef outdir
	MOCK_RESULT_DIR := "./results/%(dist)s/%(target_arch)s/"
	MOCK_SRPM_RESULT_DIR := ./results/srpm
endif

MOCK_SOURCESDIR := $(spec)
ifndef spec
	MOCK_SOURCESDIR := ./sources
endif

MOCK_SRPM := $(srpm)
ifndef srpm
	MOCK_SRPM := $(MOCK_SRPM_RESULT_DIR)/*.src.rpm
endif

distros := epel-7 fedora-26 fedora-27 fedora-28 fedora-rawhide
arches := x86_64 i386
rpm_targets := $(foreach a,$(arches),$(patsubst %,%-$a-rpm,$(distros)))

.PHONY: fetch
fetch:
	spectool -g -C $(MOCK_SOURCESDIR) $(MOCK_SOURCESDIR)/opentx-companion-2.2.1.spec

.PHONY: srpm
srpm: $(MOCK_SRPM)

$(MOCK_SRPM):
	mock --buildsrpm --spec=$(MOCK_SOURCESDIR)/opentx-companion-2.2.1.spec --sources=$(MOCK_SOURCESDIR) --resultdir=$(MOCK_SRPM_RESULT_DIR)

.PHONY: dist
dist: fetch srpm

#.PHONY: $(rpm_targets)
%-rpm: srpm
	mock --rebuild -r $* --resultdir=$(MOCK_RESULT_DIR) $(MOCK_SRPM)

.PHONY: rpm-all
rpm-all: $(rpm_targets)

.PHONY: clean
clean:
	rm -rf $(MOCK_RESULT_DIR) results

.PHONY: distclean
distclean:
	rm -rf $(MOCK_SOURCESDIR)/opentx-b55b68f.tar.gz

.PHONY: cleanall
cleanall: clean distclean

.PHONY: distall
distall: dist rpm-all

.PHONY: all
all: rpm-all
