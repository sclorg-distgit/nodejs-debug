%{?scl:%scl_package nodejs-debug}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-debug
Version:    2.2.0
Release:    5%{?dist}
Summary:    A small debugging utility for Node.js
# License text is included in Readme.md
License:    MIT
URL:        https://github.com/visionmedia/debug
Source0:    https://registry.npmjs.org/debug/-/debug-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}runtime

%description
This module is a tiny Node.js debugging utility modeled after node core's
debugging technique.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/debug
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/debug

%nodejs_symlink_deps

%files
%doc Readme.md History.md
%{nodejs_sitelib}/debug

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.0-5
- rh-nodejs8 rebuild

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.0-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.2.0-3
- Rebuilt with updated metapackage

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 2.2.0-2
- Enable scl macros

* Tue Nov 24 2015 Tom Hughes <tom@compton.nu> - 2.2.0-1
- update to 2.2.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.1-1
- update to upstream release 0.8.1

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.8.0-1
- update to upstream release 0.8.0

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.4-2
- History.md and example/ no longer included in the NPM tarball

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.4-1
- update to upstream release 0.7.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-4
- restrict to compatible arches

* Tue Jun 18 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-3
- rebuild for EL-6 to fix Provides generation

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-2
- correct a typo in the description

* Mon Feb 11 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.2-1
- initial package
