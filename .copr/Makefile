MOCK_RESULT_DIR := $(outdir)
MOCK_RESULT_DIR ?= "./results/%(dist)s/%(target_arch)s/"

ifndef srpm
	srpm := $(outdir)/*.src.rpm
endif
MOCK_SRPM := $(srpm)

fetch:
	spectool -g -C ./sources ./sources/opentx-companion-2.2.1.spec

srpm:
	mock --buildsrpm --spec ./sources/opentx-companion-2.2.1.spec --sources ./sources --resultdir=$(MOCK_RESULT_DIR)

rpm: srpm
	mock --rebuild --resultdir=$(MOCK_RESULT_DIR) $(MOCK_SRPM)

clean:
	rm -rf results sources/opentx-b55b68f.tar.gz

all: rpm
