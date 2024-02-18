Name:           hyprlang
Version:        0.4.0
Release:        1
Summary:        The official implementation library for the hypr config language.
License:        GPL3.0
Group:          Hyprland
URL:            https://github.com/hyprwm/%{name}
Source0:        https://github.com/hyprwm/hyprlang/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
Provides:       hyprlang-devel

%description
The hypr configuration language is an extremely efficient, yet easy to work with, configuration language for linux applications.
It's user-friendly, easy to grasp, and easy to implement.

%prep
%autosetup -p1
 
%build
%cmake
%make_build
 
%install
%make_install -C build

%files
%{_includedir}/hyprlang.hpp
%{_libdir}/libhyprlang.so.1
%{_libdir}/libhyprlang.so.%{version}
%{_libdir}/libhyprlang.so
%{_libdir}/pkgconfig/hyprlang.pc
