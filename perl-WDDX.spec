%define upstream_name    WDDX
%define upstream_version 1.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	WDDX.pm - Module for reading and writing WDDX packets
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a perl interface to WDDX. The latest version
of this module as well as additional information can be found at
http://www.scripted.com/wddx/. For more information about WDDX
please visit http://www.wddx.org/

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
