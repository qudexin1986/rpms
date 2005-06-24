# $Id$
# Authority: dries
# Upstream: Giuseppe Martino <denever$users,sourceforge,net>
# Upstream: <aldo-main$nongnu,org>

%{?dist: %{expand: %%define %dist 1}}

Summary: Morse tutor
Name: aldo
Version: 0.6.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.nongnu.org/aldo/

Source: http://savannah.nongnu.org/download/aldo/aldo-%{version}.tar.bz2
Patch: gcc4-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
%{?el4:BuildRequires: compat-gcc-c++}
%{?fc3:BuildRequires: compat-gcc-c++}

%description
Aldo is a morse tutor released under GPL. 
At this moment Aldo has four kinds of exercises: 
* Classic exercise: With this exercise you must guess some random 
strings of characters that Aldo plays in morse code. 
* Koch method
* Read from file: with this exercise you can write something in a text 
file and read this file with Aldo. 
Callsign exercise: with this exercise you can training yourself reciving 
random generated callsigns 

%prep
%setup
%patch -p1
%{__perl} -pi.orig -e 's| -oroot | |' Makefile */Makefile

%build
%{?el4:export CXX=g++33}
%{?fc3:export CXX=g++33}
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{?fc3:export CXX=g++33}
%makeinstall \
	PREFIX="%{buildroot}%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README.sources THANKS VERSION
%{_bindir}/aldo

%changelog
* Sat May 1 2004 Dries Verachtert <dries@ulyssis.org> 0.6.5-1
- initial package
