%include	/usr/lib/rpm/macros.perl
Summary:	Religion perl module
Summary(pl):	Modu³ perla Religion
Name:		perl-Religion
Version:	1.04
Release:	9
License:	freeware
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Religion/Religion-%{version}.tar.gz
# Source0-md5:	9e5c6edfbfc224c677089a3946bb7e27
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Religion - module to simplify installing die() and warn() handlers,
and to make such handlers easier to write and control.

%description -l pl
Religion - modu³ u³atwiaj±cy instalowanie uchwytów die() i warn() oraz
czyni±cy takie uchwyty ³atwiejszymi do napisania i kontrolowania.

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
