#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	RobotRules-Parser
Summary:	WWW::RobotRules::Parser - parse robots.txt
Summary(pl.UTF-8):   WWW::RobotRules::Parser - analiza robots.txt
Name:		perl-WWW-RobotRules-Parser
Version:	0.03
Release:	1
# "same as perl" (as in META.yml)
License:	GPLv1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2a0b81874450159fbf3fca65d3a032e9
URL:		http://search.cpan.org/dist/WWW-RobotRules-Parser/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::RobotRules::Parser allows you to simply parse robots.txt files as
described in <http://www.robotstxt.org/wc/norobots.html>. Unlike
WWW::RobotRules (which is very cool), this module does not take into
consideration your user agent name when parsing. It just parses the
structure and returns a hash containing the whole set of rules. You
can then use this to do whatever you like with it.

%description -l pl.UTF-8
WWW::RobotRules::Parser pozwala na proste analizowanie pliku
robots.txt zgodnie z opisem w
<http://www.robotstxt.org/wc/norobots.html>, a ponadto, w
przeciwieństwie do WWW::RobotRules, ten moduł nie analizuje podanej
nazwy przegladrki, a jedynie strukturę i zwraca tablicę asocjacyjną z
pełnym zestawem regułek.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/WWW/RobotRules
%{perl_vendorlib}/WWW/RobotRules/Parser.pm
%{_mandir}/man3/*
