COMMIT := a5de713b733cd56a763df1bccfc1ae13ab6da6b2
SHORTCOMMIT := $(shell c="$(COMMIT)"; echo $${c:0:7})
OPENTX_VER := 2.2.2

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
	MOCK_SRPM :=  $(MOCK_SRPM_RESULT_DIR)/opentx-companion-$(OPENTX_VER)-git_$(SHORTCOMMIT).5.fc$(shell rpm -E %fedora).src.rpm
endif

MOCK_DEBUG := "--no-cleanup-after --no-clean"
ifndef DEBUG
	MOCK_DEBUG := ""
endif

distros := fedora-26 fedora-27 fedora-28 fedora-29 fedora-rawhide
arches := x86_64 i386
rpm_targets := $(foreach a,$(arches),$(patsubst %,%-$a-rpm,$(distros)))
rpm_clean_targets := $(foreach a,$(arches),$(patsubst %,%-$a-clean,$(distros)))

MOCK_DISTGZ := $(distgz)
ifndef distgz
	MOCK_DISTGZ := sources/opentx-$(SHORTCOMMIT).tar.gz
endif

.PHONY: fetch
fetch: $(MOCK_DISTGZ)

$(MOCK_DISTGZ):
	spectool -g -C $(MOCK_SOURCESDIR) $(MOCK_SOURCESDIR)/opentx-companion-$(OPENTX_VER).spec

.PHONY: srpm
srpm: fetch $(MOCK_SRPM)

$(MOCK_SRPM):
	mock --buildsrpm $(MOCK_DEBUG) --spec=$(MOCK_SOURCESDIR)/opentx-companion-$(OPENTX_VER).spec --sources=$(MOCK_SOURCESDIR) --resultdir=$(MOCK_SRPM_RESULT_DIR)

.PHONY: dist
dist: fetch srpm

#.PHONY: $(rpm_targets)
.PHONY: %-rpm
%-rpm: srpm
	mock --rebuild -r $* $(MOCK_DEBUG) --resultdir=$(MOCK_RESULT_DIR) $(MOCK_SRPM)

.PHONY: rpm-all
rpm-all: $(rpm_targets)

#.PHONY: $(rpm_clean_targets)
%-clean:
	mock --rebuild -r $* --clean
	mock -r $* --scrub=chroot

.PHONY: clean-all
clean-all: $(rpm_clean_targets)

.PHONY: clean
clean: clean-all
	rm -rf $(MOCK_RESULT_DIR) results

.PHONY: distclean
distclean:
	rm -rf $(MOCK_DISTGZ)

.PHONY: srpmclean
srpmclean:
	rm -fr $(MOCK_SRPM)

.PHONY: cleanall
cleanall: clean distclean srpmclean

.PHONY: distall
distall: dist rpm-all

.PHONY: all
all: rpm-all
