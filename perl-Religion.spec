%include	/usr/lib/rpm/macros.perl
Summary:	Religion perl module
Summary(pl):	Modu³ perla Religion
Name:		perl-Religion
Version:	1.04
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Religion/Religion-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
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
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Religion.pm
%{_mandir}/man3/*
