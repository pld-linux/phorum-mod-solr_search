# TODO
# - imho the code needs to be reviewed is the data properly escaped when creating XML manually
%define		php_min_version 5.0.0
%define		module		solr_search
%include	/usr/lib/rpm/macros.php
Summary:	SolR Fulltext-Search Module
Name:		phorum-mod-%{module}
Version:	1.0.0
Release:	1
License:	Apache-like
Group:		Applications/WWW
Source0:	http://www.phorum.org/phorum5/file.php/62/3360/solr_search_%{version}.tar.gz
# Source0-md5:	a0b1a7e0135fcbc97eeed874376a00c2
Patch0:		use-json-ext.patch
URL:		http://www.phorum.org/phorum5/read.php?62,137055
BuildRequires:	rpm-php-pearprov
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	phorum >= 5.2
Requires:	php(date)
Requires:	php(json)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		modsdir		%{_datadir}/phorum/mods
%define		moduledir	%{modsdir}/%{module}

# no pear deps
%define		_noautopear	pear

# exclude optional php dependencies
%define		_noautophp	%{nil}

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
This module uses the solr fulltext search engine to gather the results
of the phorum-search.

%prep
%setup -qc
mv %{module}/* .
%undos -f php,txt README Changelog
%patch0 -p1

# we use json ext
%{__rm} json.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{moduledir}
cp -p *.txt *.php $RPM_BUILD_ROOT%{moduledir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%dir %{moduledir}
%{moduledir}/*.php
%{moduledir}/info.txt
