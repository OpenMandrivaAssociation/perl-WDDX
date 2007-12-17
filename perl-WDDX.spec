%define real_name WDDX

Summary:	WDDX.pm - Module for reading and writing WDDX packets
Name:		perl-%{real_name}
Version:	1.02
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:  perl-XML-Parser
BuildArch:	noarch

%description
This module provides a perl interface to WDDX. The latest version
of this module as well as additional information can be found at
http://www.scripted.com/wddx/. For more information about WDDX
please visit http://www.wddx.org/

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/WDDX
%{perl_vendorlib}/WDDX/*
%{perl_vendorlib}/WDDX.pm
%{_mandir}/*/*

