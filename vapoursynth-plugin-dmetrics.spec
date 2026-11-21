Summary:	Decomb Metrics plugin for Vapoursynth
Summary(pl.UTF-8):	Wtyczka Decomb Metrics dla programu Vapoursynth
Name:		vapoursynth-plugin-dmetrics
Version:	2
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/vapoursynth/dmetrics/releases
Source0:	https://github.com/vapoursynth/dmetrics/archive/R%{version}/dmetrics-R%{version}.tar.gz
# Source0-md5:	8b1b1f522430b624c6cec1c87b78e714
Patch0:		dmetrics-python3.patch
URL:		https://github.com/vapoursynth/dmetrics
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	meson >= 1.2.3
BuildRequires:	ninja >= 1.5
BuildRequires:	python3 >= 1:3.12
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	vapoursynth-devel >= 74
Requires:	vapoursynth >= 74
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
%patch -P0 -p1

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitedir}/vapoursynth/plugins/dmetrics.so
