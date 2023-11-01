%global commit 4f5c45238ef77e5d6b88bc403432bd59de7efde9
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           plotnetcfg
Version:        0.4.1
Release:        18%{?dist}
Summary:        A tool to plot network configuration

License:        GPLv2+
URL:            https://github.com/jbenc/plotnetcfg
Source0:        https://github.com/jbenc/plotnetcfg/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Patch0:		0001-Pass-LDFLAGS-to-the-linker.patch

BuildRequires: make
BuildRequires:  gcc, jansson-devel
Requires:       jansson

%description
plotnetcfg is a tool that output a diagram of network configuration on the
host in a form suitable for graphviz.

%prep
%autosetup -n %{name}-%{commit}

%build
%set_build_flags
make %{?_smp_mflags} CFLAGS="%{build_cflags}" LDFLAGS="%{build_ldflags}"

%install
%make_install

%files
%license COPYING
%doc README
%{_sbindir}/plotnetcfg
%{_mandir}/man5/*
%{_mandir}/man8/*

%changelog
* Thu Feb 17 2022 Jiri Benc <jbenc@redhat.com> - 0.4.1-18
- Fixed build flags [2044887]

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.4.1-17
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.4.1-16
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Jiri Benc <jbenc@redhat.com> - 0.4.1-9
- added gcc to BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 27 2015 Jiri Benc <jbenc@redhat.com> - 0.4.1-2
- clarified the current license

* Mon Jul 27 2015 Jiri Benc <jbenc@redhat.com> - 0.4.1-1
- updated to v0.4.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Jiri Benc <jbenc@redhat.com> - 0.3-1
- initial packaging
