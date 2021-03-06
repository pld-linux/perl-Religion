%define		pdir	Religion
Summary:	Religion Perl module
Summary(pl.UTF-8):	Moduł Perla Religion
Name:		perl-Religion
Version:	1.04
Release:	10
License:	Freeware
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Religion/Religion-%{version}.tar.gz
# Source0-md5:	9e5c6edfbfc224c677089a3946bb7e27
URL:		http://search.cpan.org/dist/Religion/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Religion - module to simplify installing die() and warn() handlers,
and to make such handlers easier to write and control.

%description -l pl.UTF-8
Religion - moduł ułatwiający instalowanie uchwytów die() i warn() oraz
czyniący takie uchwyty łatwiejszymi do napisania i kontrolowania.

%prep
%setup -q -n Religion-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Religion.pm
%{_mandir}/man3/*
