Name:       ocaml-tsdl
Version:    1904fb
Release:    %mkrel 1
Summary:    Thin OCaml bindings to SDL2
Group:      Development/OCaml
License:    BSD-3-Clause
URL:        http://erratique.ch/software/tsdl/
#Project:   https://github.com/dbuenzli/tsdl
Source0:    tsdl-%{version}.tar.gz

BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ctypes
BuildRequires:  pkgconfig(sdl2)

%description
CTypes based OCaml bindings to the SDL2.

%package    devel
Summary:    Development files for %{name}
Group:      Development/OCaml
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development modules you need to use %{name} in
your programs.

%prep
%setup -q -n tsdl-%{version}

%build
./pkg/pkg-git
./pkg/build true

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/tsdl
cd _build/src/
ocamlfind install tsdl ../pkg/META \
  *.a *.cm[iatx] *.cmx[as] *.cmti *.mli *.so

%files
%doc README.md CHANGES.md TODO.md
%dir %{_libdir}/ocaml/tsdl
%{_libdir}/ocaml/tsdl/META
%{_libdir}/ocaml/tsdl/*.cmi
%{_libdir}/ocaml/tsdl/*.cma
%{_libdir}/ocaml/tsdl/*.cmxs
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%doc doc/
%doc test/
%{_libdir}/ocaml/tsdl/*.a
%{_libdir}/ocaml/tsdl/*.cmxa
%{_libdir}/ocaml/tsdl/*.cmx
%{_libdir}/ocaml/tsdl/*.cmt
%{_libdir}/ocaml/tsdl/*.cmti
%{_libdir}/ocaml/tsdl/*.mli
