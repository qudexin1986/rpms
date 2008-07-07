# $Id$
# Authority: dries
# Upstream: Randy J Ray <rjray$blackperl,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RPC-XML

Summary: Set of classes for core data, message and XML handling
Name: perl-RPC-XML
Version: 0.60
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RPC-XML/

Source: http://www.cpan.org/modules/by-module/RPC/RPC-XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl-libwww-perl
BuildRequires: perl(ExtUtils::MakeMaker)
### Apparently I used the wrong name: XML-RPC doesn't exist, it's RPC-XML
Obsoletes: perl-XML-RPC

%description
The RPC::XML package is an implementation of XML-RPC. The module provides
classes for sample client and server implementations, a server designed as
an Apache location-handler, and a suite of data-manipulation classes that
are used by them.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog ChangeLog.xml MANIFEST META.yml README README.apache2 SIGNATURE
%doc %{_mandir}/man1/make_method.1*
#%doc %{_mandir}/man3/*
%doc %{_mandir}/man3/Apache::RPC::*.3pm*
%doc %{_mandir}/man3/RPC::XML.3pm*
%doc %{_mandir}/man3/RPC::XML::*.3pm*
%{_bindir}/make_method
%dir %{perl_vendorlib}/auto/RPC/
%{perl_vendorlib}/auto/RPC/XML/
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/RPC
%dir %{perl_vendorlib}/RPC/
%{perl_vendorlib}/RPC/XML/
%{perl_vendorlib}/RPC/XML.pm

%changelog
* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 0.60-1
- Updated to release 0.60.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.59-1
- Updated to release 0.59.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Sat Jan  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.57-1
- Initial package.