%global tl_name pseudo
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.3
Release:	%{tl_revision}.1
Summary:	Straightforward pseudocode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pseudo
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pseudo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package permits writing pseudocode without much fuss and with quite
a bit of configurability. Its main environment combines aspects of
enumeration, tabbing and tabular for nonintrusive line numbering,
indentation and highlighting, and there is functionality for typesetting
common syntactic elements such as keywords, identifiers, and comments.
The package relies on aliascnt, array, colortbl, expl3, l3keys2e,
xcolor, and xparse.

