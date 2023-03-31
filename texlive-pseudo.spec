Name:		texlive-pseudo
Version:	64182
Release:	2
Summary:	Straightforward pseudocode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pseudo
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package permits writing pseudocode without much fuss and
with quite a bit of configurability. Its main environment
combines aspects of enumeration, tabbing and tabular for
nonintrusive line numbering, indentation and highlighting, and
there is functionality for typesetting common syntactic
elements such as keywords, identifiers, and comments. The
package relies on aliascnt, array, colortbl, expl3, l3keys2e,
xcolor, and xparse.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pseudo
%doc %{_texmfdistdir}/doc/latex/pseudo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
