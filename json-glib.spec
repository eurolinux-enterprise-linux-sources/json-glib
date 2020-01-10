%define glib_ver 2.37.6

Name:		json-glib
Version:	1.2.6
Release:	1%{?dist}
Summary:	Library for JavaScript Object Notation format

Group:		System Environment/Libraries
License:	LGPLv2+
URL:		https://wiki.gnome.org/Projects/JsonGlib
#VCS:		git:git://git.gnome.org/json-glib
Source0:	http://download.gnome.org/sources/%{name}/1.2/%{name}-%{version}.tar.xz

BuildRequires:	docbook-style-xsl
BuildRequires:	glib2-devel >= %{glib_ver}
BuildRequires:	gobject-introspection-devel
BuildRequires:	/usr/bin/xsltproc


%description
%{name} is a library providing serialization and deserialization support
for the JavaScript Object Notation (JSON) format.


%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}%{_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tests
Summary: Tests for the json-glib package
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The json-glib-tests package contains tests that can be used to verify
the functionality of the installed json-glib package.

%prep
%setup -q -n %{name}-%{version}


%build
%configure --enable-static=no --enable-installed-tests
make %{?_smp_mflags} V=1


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang json-glib-1.0

%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files -f json-glib-1.0.lang
%doc NEWS
%license COPYING
%{_libdir}/lib%{name}*.so.*
%{_libdir}/girepository-1.0/Json-1.0.typelib

%files devel
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/%{name}-1.0.pc
%{_includedir}/%{name}-1.0/
%{_datadir}/gtk-doc/
%{_datadir}/gir-1.0/Json-1.0.gir
%{_bindir}/json-glib-format
%{_bindir}/json-glib-validate
%{_mandir}/man1/json-glib-format.1*
%{_mandir}/man1/json-glib-validate.1*

%files tests
%{_libexecdir}/installed-tests/%{name}
%{_datadir}/installed-tests

%changelog
* Mon Mar 13 2017 Kalev Lember <klember@redhat.com> - 1.2.6-1
- Update to 1.2.6
- Resolves: #1386996

* Mon Aug 01 2016 Kalev Lember <klember@redhat.com> - 1.2.2-1
- Update to 1.2.2
- Resolves: #1386996

* Fri May 30 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.2-1
- Update to 1.0.2
- Resolves: #1174501

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.16.0-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.16.0-2
- Mass rebuild 2013-12-27

* Tue Apr 16 2013 Kalev Lember <kalevlember@gmail.com> - 0.16.0-1
- Update to 0.16.0
- Don't depend on gtk-doc (#604377)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 17 2012 Richard Hughes <hughsient@gmail.com> - 0.15.2-1
- Update to 0.15.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 0.14.2-1
- Update to 0.14.2

* Mon Sep 19 2011 Matthias Clasen <mclasen@redhat.com> - 0.14.0-1
- Update to 0.14.0

* Wed Sep  7 2011 Owen Taylor <otaylor@redhat.com> - 0.13.90-1
- Update to 0.13.90

* Thu Jun 16 2011 Alex Hudson <fedora@alexhudson.com> - 0.12.6-1
- Update to 0.12.6
- Remove gtk-doc dependency for bug 604377

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 29 2010 Owen Taylor <otaylor@redhat.com> - 0.12-1
- Update to 0.12.0

* Wed Sep 29 2010 jkeating - 0.11.3-0.2.git19b0b87
- Rebuilt for gcc bug 634757

* Wed Sep 22 2010 Matthias Clasen <mclasen@redhat.com> - 0.11.3-0.1.git19b0b87
- git snapshot

* Tue Sep 21 2010 Matthias Clasen <mclasen@redhat.com> - 0.10.4-4
- Rebuild with newer gobject-introspection

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 0.10.4-3
- Rebuild with new gobject-introspection

* Thu Jul  1 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.10.4-2
- Rebuild for "Incompatible version 1.0 (supported: 1.1)"
  for introspection file

* Fri Mar 19 2010 Brian Pepple <bpepple@fedoraproject.org> - 0.10.4-1
- Update to 0.10.4.

* Wed Jan 27 2010 Peter Robinson <pbrobinson@gmail.com> - 0.10.0-3
- Require the gobject-introspection-devel package, not the library

* Wed Jan 27 2010 Peter Robinson <pbrobinson@gmail.com> - 0.10.0-2
- Enable gobject-introspection support

* Tue Dec 29 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0.

* Mon Nov 16 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.8.2-1
- Update to 0.8.2.

* Tue Sep 29 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0.
- Update source url.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Brian Pepple <bpepple@fedoraproject.org> - 0.6.2-3
- Disable tests for now.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat May 31 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2.
- Enable tests.

* Mon May 19 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.6.0-1
- Update 0.6.0.
- Disable tests for now.
- Add requires on gtk-doc.

* Sun Apr 20 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.4.0-1
- Initial Fedora spec.

