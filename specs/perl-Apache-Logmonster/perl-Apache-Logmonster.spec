# $Id$
# Authority: dag
# Upstream: Matt Simerson <matt,simerson$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Logmonster

Summary: Apache log file splitter, processor, sorter, etc
Name: perl-Apache-Logmonster
Version: 3.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Logmonster/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Logmonster-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Compress::Zlib) >= 2.0
BuildRequires: perl(Date::Parse) >= 2.0
BuildRequires: perl(Module::Build)
BuildRequires: perl(Params::Validate) >= 0.8

%description
Apache log file splitter, processor, sorter, etc.

%prep
%setup -n %{real_name}-%{version}

%build
#%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
#%{__make} %{?_smp_mflags}
%{__perl} Build.PL
./Build

%install
%{__rm} -rf %{buildroot}
#%{__make} pure_install
PERL_INSTALL_ROOT="%{buildroot}" ./Build install installdirs="vendor"

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes FAQ INSTALL MANIFEST MANIFEST.SKIP META.yml README TODO doc/ examples/
#%doc %{_mandir}/man1/logmonster.pl.1*
%doc %{_mandir}/man3/Apache::Logmonster.3pm*
%doc %{_mandir}/man3/Apache::Logmonster::Perl.3pm*
%doc %{_mandir}/man3/Apache::Logmonster::Utility.3pm*
%doc %{_mandir}/man3/Regexp::Log::Monster.3pm*
%dir %{perl_vendorlib}/Apache/
%{perl_vendorlib}/Apache/Logmonster/
%{perl_vendorlib}/Apache/Logmonster.pm
#%{perl_vendorlib}/Apache/logmonster.pl
%dir %{perl_vendorlib}/Regexp/Log/
%{perl_vendorlib}/Regexp/Log/Monster.pm
#%{perl_vendorlib}/Regexp/Log.pm
%exclude %{_bindir}/install_freebsd_deps.sh

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 3.04-1
- Updated to release 3.04.

* Mon Aug 20 2007 Christoph Maser <cmr$financial,com> - 3.03-1
- Initial package. (using DAR)