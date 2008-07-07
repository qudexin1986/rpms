# $Id$
# Authority: dag
# Upstream: Torsten Schönfeld <kaffeetisch$gmx,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Gtk2-GladeXML

Summary: Perl module to create user interfaces directly from Glade XML files
Name: perl-Gtk2-GladeXML
Version: 1.006
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Gtk2-GladeXML/

Source: http://www.cpan.org/modules/by-module/Gtk2/Gtk2-GladeXML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Glib::MakeHelper)
BuildRequires: perl(Gtk2)
BuildRequires: pkgconfig
BuildRequires: libglade2-devel
BuildRequires: perl(Cairo::Install::Files)
Requires: perl >= 2:5.8.0

%description
Gtk2-GladeXML is a Perl module to create user interfaces
directly from Glade XML files.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE MANIFEST META.yml NEWS README
%doc %{_mandir}/man3/Gtk2::GladeXML.3pm*
%dir %{perl_vendorarch}/Gtk2/
%{perl_vendorarch}/Gtk2/GladeXML.pm
%{perl_vendorarch}/Gtk2/GladeXML/
%dir %{perl_vendorarch}/auto/Gtk2/
%{perl_vendorarch}/auto/Gtk2/GladeXML/

%changelog
* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 1.006-1
- Initial package. (using DAR)