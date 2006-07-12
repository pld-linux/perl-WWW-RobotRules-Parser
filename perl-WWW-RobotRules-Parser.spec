#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	RobotRules-Parser
Summary:	perl(WWW::RobotRules-Parser)
Name:		perl-WWW-RobotRules-Parser
Version:	0.02
Release:	0.2
# "same as perl" (as in META.yml
License:	GPLv1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a7b77fdd5084de92522bacb2049ef254
Patch0:		%{name}-Makefile.PL.patch
URL:		http://search.cpan.org/dist/WWW-RobotRules-Parser
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_noautoreq	'perl(anything_fake_or_conditional)'

%description
WWW::RobotRules::Parser allows you to simply parse robots.txt files as
described in http://www.robotstxt.org/wc/norobots.html. Unlike WWW::RobotRules
(which is very cool), this module does not take into consideration your user
agent name when parsing. It just parses the structure and returns a hash
containing the whole set of rules. You can then use this to do whatever you
like with it.

%description -l pl
WWW::RobotRules::Parser pozwala na proste parsowanie pliku robot.txt jak opisano w
http://www.robotstxt.org/wc/norobots.html, ponadto w przeciwienstwie do WWW::RobotRules
ten modul nie analizuje podanej nazwy przegladrki, a jedynnie parsuje strukture i zwraca
tablice asocjacyjna z pełnym zestawem regółek.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
# disable broken test
mv t/99-pod-coverage.t t/99-pod-coverage.t.disabled
grep -v 99-pod-coverage.t < MANIFEST >MANIFEST.mod
mv -f MANIFEST.mod MANIFEST

%build
# Don't use pipes here: they generally don't work. Apply a patch.
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
%{perl_vendorlib}/WWW/RobotRules/Parser.pm
%{_mandir}/man3/*
