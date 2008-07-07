# $Id$
# Authority: dries
# Upstream: Marty Pauley <kasei$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor

Summary: Automated accessor generation
Name: perl-Class-Accessor
Version: 0.31
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor/

Source: http://www.cpan.org/modules/by-module/Class/Class-Accessor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module automagically generates accessor/mutators for your class.

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
%doc Changes README
%doc %{_mandir}/man3/Class::Accessor*.3pm*
%{perl_vendorlib}/Class/Accessor.pm
%{perl_vendorlib}/Class/Accessor/

%changelog
* Mon Aug 20 2007 Christoph Maser <cmr$financial,com>  - 0.31-1
- Updated to release 0.31.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.30-1
- Updated to release 0.30.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.27-1
- Updated to release 0.27.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.22-1
- Updated to release 0.22.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Initial package.