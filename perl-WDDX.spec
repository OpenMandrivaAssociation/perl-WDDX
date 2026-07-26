%define upstream_name    WDDX
Name:		perl-%{upstream_name}
Version:	1.02
Release:	6

Summary:	WDDX.pm - Module for reading and writing WDDX packets
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://metacpan.org/dist/WDDX
Source0:	https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/WDDX-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
This module provides a perl interface to WDDX. The latest version
of this module as well as additional information can be found at
http://www.scripted.com/wddx/. For more information about WDDX
please visit http://www.wddx.org/

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/WDDX
%{perl_vendorlib}/WDDX/*
%{perl_vendorlib}/WDDX.pm
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.20.0-1mdv2010.0
+ Revision: 401918
- rebuild using %1.02 Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.02-6mdv2009.0
+ Revision: 258783
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.02-5mdv2009.0
+ Revision: 246697
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.02-3mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 1.02-3mdv2008.0
+ Revision: 23588
- rebuild


* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.02-2mdk
- Fix BuildRequires

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.02-1mdk
- initial Mandriva package

