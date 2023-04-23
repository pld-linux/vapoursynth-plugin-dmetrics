Summary:	Decomb Metrics plugin for Vapoursynth
Summary(pl.UTF-8):	Wtyczka Decomb Metrics dla programu Vapoursynth
Name:		vapoursynth-plugin-dmetrics
Version:	1
Release:	1
License:	GPL v2+
Group:		Libraries
%define	gitref	acdeca22038583d73d420ccf76d0658f06cae3c0
Source0:	https://github.com/vapoursynth/dmetrics/archive/R%{version}/dmetrics-R%{version}.tar.gz
# Source0-md5:	44291a66169ac65cac666adefbb59c6a
URL:		https://github.com/vapoursynth/dmetrics
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	vapoursynth-devel >= 55
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Decomb Metrics plugin attaches the match metrics calculated by
Telecide (decomb package) to frames as properties. Primarily intended
for use with Wobbly. Requires YUV420P8 input.

%description -l pl.UTF-8
Wtyczka Decomb Metrics dołącza do ramek jako własności miary dopasowań
obliczone przez Telecide (pakiet decomb). Przeznaczone głównie do
użycia z Wobbly. Wymaga wejścia YUV420P8.

%prep
%setup -q -n dmetrics-R%{version}

%build
libtool --tag=CXX --mode=compile %{__cxx} -c -o src/dmetrics.lo %{rpmcflags} %{rpmcppflags} $(pkg-config --cflags vapoursynth) src/dmetrics.cpp
libtool --tag=CXX --mode=link %{__cxx} -shared -module -avoid-version -o src/libdmetrics.la %{rpmldflags} %{rpmcflags} src/dmetrics.lo -rpath %{_libdir}/vapoursynth

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/vapoursynth

libtool --mode=install install src/libdmetrics.la $RPM_BUILD_ROOT%{_libdir}/vapoursynth

%{__rm} $RPM_BUILD_ROOT%{_libdir}/vapoursynth/libdmetrics.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/vapoursynth/libdmetrics.so
