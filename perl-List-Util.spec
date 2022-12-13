#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-List-Util
Version  : 1.63
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Scalar-List-Utils-1.63.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Scalar-List-Utils-1.63.tar.gz
Summary  : 'Common Scalar and List utility subroutines'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-List-Util-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This distribution is a replacement for the builtin distribution.
This package contains a selection of subroutines that people have
expressed would be nice to have in the perl core, but the usage would not
really be high enough to warrant the use of a keyword, and the size so
small such that being individual extensions would be wasteful.

%package dev
Summary: dev components for the perl-List-Util package.
Group: Development
Provides: perl-List-Util-devel = %{version}-%{release}
Requires: perl-List-Util = %{version}-%{release}

%description dev
dev components for the perl-List-Util package.


%package perl
Summary: perl components for the perl-List-Util package.
Group: Default
Requires: perl-List-Util = %{version}-%{release}

%description perl
perl components for the perl-List-Util package.


%prep
%setup -q -n Scalar-List-Utils-1.63
cd %{_builddir}/Scalar-List-Utils-1.63

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/List::Util.3
/usr/share/man/man3/List::Util::XS.3
/usr/share/man/man3/Scalar::Util.3
/usr/share/man/man3/Sub::Util.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
