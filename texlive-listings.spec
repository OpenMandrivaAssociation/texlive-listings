%global tl_name listings
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.11b
Release:	%{tl_revision}.1
Summary:	Typeset source code listings using LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/listings
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listings.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listings.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/listings.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to typeset programs (programming code)
within LaTeX; the source code is read directly by TeX--no front-end
processor is needed. Keywords, comments and strings can be typeset using
different styles (default is bold for keywords, italic for comments and
no special style for strings). Support for hyperref is provided. To use,
\usepackage{listings}, identify the language of the object to typeset,
using a construct like: \lstset{language=Python}, then use environment
lstlisting for inline code. External files may be formatted using
\lstinputlisting to process a given file in the form appropriate for the
current language. Short (in-line) listings are also available, using
either \lstinline|...| or |...| (after defining the | token with the
\lstMakeShortInline command).

