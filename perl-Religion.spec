%include	/usr/lib/rpm/macros.perl
Summary:	Religion perl module
Summary(pl):	Modu� perla Religion
Name:		perl-Religion
Version:	1.04
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Religion/Religion-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Religion - module to simplify installing die() and warn() handlers, 
and to make such handlers easier to write and control. 

%description -l pl
Religion - modu� u�atwiaj�cy instalowanie uchwyt�w die() i warn() oraz
czyni�cy takie uchwyty �atwiejszymi do napisania i kontrolowania.

%prep
%setup -q -n Religion-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Religion
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Religion.pm
%{perl_sitearch}/auto/Religion

%{_mandir}/man3/*
