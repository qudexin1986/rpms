# $Id$
# Authority: dag
# Upstream: Gisle Aas <gisle$ActiveState,com>

### RHEL ships with perl-URI already
# ExclusiveDist: none

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name URI

Summary: Perl module that implements Uniform Resource Identifiers (absolute and relative)
Name: perl-URI
Version: 1.36
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/URI/

Source: http://www.cpan.org/modules/by-module/URI/URI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-URI is a Perl module that implements Uniform Resource Identifiers.
(absolute and relative)

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
%doc Changes MANIFEST META.yml README rfc2396.txt
%doc %{_mandir}/man3/URI.3pm*
%doc %{_mandir}/man3/URI::*.3pm*
%{perl_vendorlib}/URI/
%{perl_vendorlib}/URI.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 1.36-1
- Updated to release 1.36.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.35-1
- Initial package. (using DAR)